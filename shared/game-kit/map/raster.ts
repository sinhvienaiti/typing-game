export interface RasterGrid {
  readonly originX: number; // cm, west edge of cell column 0
  readonly originZ: number; // cm, north edge of cell row 0
  readonly cellCm: number; // even, >= 2
  readonly w: number; // cells along x
  readonly h: number; // cells along z
}

export type RasterPoint = readonly [number, number]; // [x, z] in cm
export const RASTER_LIMIT_CM = 16384;
export const RASTER_MAX_HALF_WIDTH_CM = 2000;

function integerIn(value: number, min: number, max: number): void {
  if (!Number.isSafeInteger(value) || value < min || value > max) {
    throw new RangeError("Raster value outside integer bounds");
  }
}

function validateGrid(grid: RasterGrid): void {
  integerIn(grid.originX, -RASTER_LIMIT_CM, RASTER_LIMIT_CM);
  integerIn(grid.originZ, -RASTER_LIMIT_CM, RASTER_LIMIT_CM);
  integerIn(grid.cellCm, 2, 2 * RASTER_LIMIT_CM);
  integerIn(grid.w, 1, 4096);
  integerIn(grid.h, 1, 4096);
  if (grid.cellCm / 2 !== Math.floor(grid.cellCm / 2)
    || grid.originX + grid.w * grid.cellCm > RASTER_LIMIT_CM
    || grid.originZ + grid.h * grid.cellCm > RASTER_LIMIT_CM) {
    throw new RangeError("Invalid raster grid extent or cell size");
  }
}

function validateMask(grid: RasterGrid, mask: Uint8Array): void {
  validateGrid(grid);
  if (mask.length !== grid.w * grid.h) throw new RangeError("Invalid raster mask length");
}

function coordinate(value: number): void {
  integerIn(value, -RASTER_LIMIT_CM, RASTER_LIMIT_CM);
}

function validatePoints(points: readonly RasterPoint[], minLength: number): void {
  if (points.length < minLength) throw new RangeError("Too few raster points");
  for (const [x, z] of points) {
    coordinate(x);
    coordinate(z);
  }
}

export function makeMask(grid: RasterGrid): Uint8Array {
  validateGrid(grid);
  return new Uint8Array(grid.w * grid.h);
}

export function cellCenterX(grid: RasterGrid, i: number): number {
  validateGrid(grid);
  integerIn(i, 0, grid.w - 1);
  return grid.originX + i * grid.cellCm + grid.cellCm / 2;
}

export function cellCenterZ(grid: RasterGrid, j: number): number {
  validateGrid(grid);
  integerIn(j, 0, grid.h - 1);
  return grid.originZ + j * grid.cellCm + grid.cellCm / 2;
}

// Clip inclusive world bounds to indices whose cell centers lie inside them.
function bounds(grid: RasterGrid, x0: number, z0: number, x1: number, z1: number): readonly [number, number, number, number] {
  const cx0 = grid.originX + grid.cellCm / 2;
  const cz0 = grid.originZ + grid.cellCm / 2;
  return [
    Math.max(0, Math.ceil((x0 - cx0) / grid.cellCm)),
    Math.max(0, Math.ceil((z0 - cz0) / grid.cellCm)),
    Math.min(grid.w - 1, Math.floor((x1 - cx0) / grid.cellCm)),
    Math.min(grid.h - 1, Math.floor((z1 - cz0) / grid.cellCm)),
  ];
}

export function rasterDisc(grid: RasterGrid, mask: Uint8Array, x: number, z: number, r: number): void {
  validateMask(grid, mask);
  coordinate(x);
  coordinate(z);
  integerIn(r, 0, 32768);
  const [i0, j0, i1, j1] = bounds(grid, x - r, z - r, x + r, z + r);
  for (let j = j0; j <= j1; j += 1) {
    const dz = grid.originZ + j * grid.cellCm + grid.cellCm / 2 - z;
    for (let i = i0; i <= i1; i += 1) {
      const dx = grid.originX + i * grid.cellCm + grid.cellCm / 2 - x;
      if (dx * dx + dz * dz <= r * r) mask[j * grid.w + i] = 1;
    }
  }
}

export function rasterRect(grid: RasterGrid, mask: Uint8Array, x0: number, z0: number, x1: number, z1: number): void {
  validateMask(grid, mask);
  coordinate(x0);
  coordinate(z0);
  coordinate(x1);
  coordinate(z1);
  if (x0 > x1 || z0 > z1) throw new RangeError("Reversed raster rectangle");
  const [i0, j0, i1, j1] = bounds(grid, x0, z0, x1, z1);
  for (let j = j0; j <= j1; j += 1) {
    for (let i = i0; i <= i1; i += 1) mask[j * grid.w + i] = 1;
  }
}

/*
 * All coordinates, including cell centers, lie in [-16384, 16384], and
 * halfWidth <= 2000. Differences are <= 32768; products of two differences
 * are <= 2^30 and sums of two products are < 2^32, so they are exact.
 * halfWidth^2 * len2 <= 2000^2 * 2 * 32768^2, about 8.6e15 < 2^53,
 * is also exact. Only c*c may exceed 2^53. In that case it is necessarily
 * larger than halfWidth^2 * len2, and monotonic rounding preserves the comparison.
 */
export function rasterPolyline(grid: RasterGrid, mask: Uint8Array, points: readonly RasterPoint[], halfWidth: number): void {
  validateMask(grid, mask);
  validatePoints(points, 1);
  integerIn(halfWidth, 0, RASTER_MAX_HALF_WIDTH_CM);
  const hw2 = halfWidth * halfWidth;
  for (let segment = 0; segment < Math.max(1, points.length - 1); segment += 1) {
    const [ax, az] = points[segment]!;
    const [bx, bz] = points[Math.min(segment + 1, points.length - 1)]!;
    const dx = bx - ax;
    const dz = bz - az;
    const len2 = dx * dx + dz * dz;
    const [i0, j0, i1, j1] = bounds(grid,
      Math.min(ax, bx) - halfWidth, Math.min(az, bz) - halfWidth,
      Math.max(ax, bx) + halfWidth, Math.max(az, bz) + halfWidth);
    for (let j = j0; j <= j1; j += 1) {
      const pz = grid.originZ + j * grid.cellCm + grid.cellCm / 2;
      for (let i = i0; i <= i1; i += 1) {
        const px = grid.originX + i * grid.cellCm + grid.cellCm / 2;
        const ux = px - ax;
        const uz = pz - az;
        const t = ux * dx + uz * dz;
        let inside: boolean;
        if (len2 === 0 || t <= 0) {
          inside = ux * ux + uz * uz <= hw2;
        } else if (t >= len2) {
          const vx = px - bx;
          const vz = pz - bz;
          inside = vx * vx + vz * vz <= hw2;
        } else {
          const c = ux * dz - uz * dx;
          inside = c * c <= hw2 * len2;
        }
        if (inside) mask[j * grid.w + i] = 1;
      }
    }
  }
}

export function rasterPolygon(grid: RasterGrid, mask: Uint8Array, points: readonly RasterPoint[]): void {
  validateMask(grid, mask);
  validatePoints(points, 3);
  let x0 = RASTER_LIMIT_CM;
  let z0 = RASTER_LIMIT_CM;
  let x1 = -RASTER_LIMIT_CM;
  let z1 = -RASTER_LIMIT_CM;
  for (const [x, z] of points) {
    x0 = Math.min(x0, x);
    z0 = Math.min(z0, z);
    x1 = Math.max(x1, x);
    z1 = Math.max(z1, z);
  }
  const [i0, j0, i1, j1] = bounds(grid, x0, z0, x1, z1);
  for (let j = j0; j <= j1; j += 1) {
    const pz = grid.originZ + j * grid.cellCm + grid.cellCm / 2;
    for (let i = i0; i <= i1; i += 1) {
      const px = grid.originX + i * grid.cellCm + grid.cellCm / 2;
      let inside = false;
      for (let edge = 0; edge < points.length; edge += 1) {
        const [ax, az] = points[edge]!;
        const [bx, bz] = points[edge + 1 === points.length ? 0 : edge + 1]!;
        const cross = (bx - ax) * (pz - az) - (bz - az) * (px - ax);
        if (cross === 0 && Math.min(ax, bx) <= px && px <= Math.max(ax, bx)
          && Math.min(az, bz) <= pz && pz <= Math.max(az, bz)) {
          inside = true;
          break;
        }
        if ((az > pz) !== (bz > pz)) {
          const den = bz - az;
          const num = (pz - az) * (bx - ax);
          const lhs = (px - ax) * den;
          if (den > 0 ? lhs < num : lhs > num) inside = !inside;
        }
      }
      if (inside) mask[j * grid.w + i] = 1;
    }
  }
}
