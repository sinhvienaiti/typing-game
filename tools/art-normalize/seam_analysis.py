"""Đường nối quy hoạch động và đối chiếu tọa độ nguồn, chỉ dùng thư viện chuẩn."""
import math
import statistics


def rows(w, h, pixels, axis):
    if axis == 'x':
        return [pixels[y*w*4:(y+1)*w*4] for y in range(h)]
    return [bytes(pixels[(y*w+x)*4+c] for y in range(h) for c in range(4)) for x in range(w)]


def minimum_path(data, band):
    length = len(data[0])//4
    shift = length-band
    lo, hi = 5, band-5
    if hi <= lo:
        lo, hi = 1, max(2,band-1)
    parents = []
    previous = None
    for row in data:
        costs = []
        for k in range(lo,hi):
            error=sum((row[(shift+k)*4+c]-row[k*4+c])**2 for c in range(3))
            a,b=max(0,k-4),min(band-1,k+4)
            cross=sum(abs(row[(shift+a)*4+c]-row[b*4+c]) for c in range(3))/3
            costs.append(error+60*cross**2)
        if previous is None:
            previous = costs
            parents.append([0]*len(costs))
            continue
        current, parent = [], []
        for k,cost in enumerate(costs):
            q = min(range(max(0,k-4),min(len(costs),k+5)),key=lambda j:previous[j])
            current.append(cost+previous[q]);parent.append(q)
        previous = current;parents.append(parent)
    k = min(range(len(previous)), key=previous.__getitem__)
    path = []
    for parent in reversed(parents):
        path.append(k+lo);k=parent[k]
    return path[::-1]


def infer_path(data, source, band):
    """Least residual split locates even a hard/wrong cut; never trusts metadata."""
    shift = len(data[0])//4
    result=[]
    for row,ref in zip(data,source):
        left=[sum(abs(row[k*4+c]-ref[(shift+k)*4+c]) for c in range(3)) for k in range(band)]
        right=[sum(abs(row[k*4+c]-ref[k*4+c]) for c in range(3)) for k in range(band)]
        score=sum(right);best=(score,0)
        for k in range(band):
            score+=left[k]-right[k]
            if score<best[0]:best=(score,k+1)
        approximate=min(band-1,max(1,best[1]))
        radius=max(1,min(3,band//8))
        def error(cut):
            total=0
            for k in range(max(0,approximate-6),min(band,approximate+7)):
                t=min(1,max(0,(k-cut+radius)/(2*radius)));t=t*t*(3-2*t)
                total+=sum(abs(row[k*4+c]-round(ref[(shift+k)*4+c]*(1-t)+ref[k*4+c]*t)) for c in range(3))
            return total
        result.append(min(range(max(1,approximate-4),min(band,approximate+5)),key=error))
    return result


def laps(data):
    length=len(data[0])//4
    return [statistics.mean(abs(row[(k-1)*4+c]-2*row[k*4+c]+row[(k+1)*4+c])
                            for row in data for c in range(3)) for k in range(1,length-1)]


def row_residual(data, band, source=None, path=None, radius=3):
    length=len(data[0])//4
    window=min(30,max(2,band))
    peak=0
    for y in range(len(data)-1):
        a,b=data[y],data[y+1]
        for c in range(3):
            diffs=[]
            for k in range(length):
                delta=b[k*4+c]-a[k*4+c]
                if source is not None:
                    # Corresponding source column for EACH row, also along a moving seam.
                    def expected(line):
                        if not path or k>=band:return source[line][k*4+c]
                        t=min(1,max(0,(k-path[line]+radius)/(2*radius)))
                        t=t*t*(3-2*t)
                        return source[line][(length+k)*4+c]*(1-t)+source[line][k*4+c]*t
                    delta-=expected(y+1)-expected(y)
                diffs.append(delta)
            inner=statistics.mean(diffs[band:length-band]) if length>2*band else 0
            prefix=[0]
            for v in diffs:prefix.append(prefix[-1]+v)
            for start in range(0,length-window+1):
                if start<band or start+window>length-band:
                    step=(prefix[start+window]-prefix[start])/window
                    peak=max(peak,abs(step)-(abs(inner) if source is None else 0))
    return peak


def cut_metrics(data, source, band, path, radius=3):
    length=len(data[0])//4
    span=2*radius+2
    records=[]
    # Row bands expose mountain breaks hidden by the full-height mean.
    for y0 in range(0,len(data),64):
        ys=range(y0,min(y0+64,len(data)))
        controls=[];lum_controls=[]
        lum=lambda row,pos:sum(row[pos*4+c]*v for c,v in enumerate((.2126,.7152,.0722)))
        for k in range(band,length-span):
            controls.append(statistics.mean(abs(data[y][k*4+c]-data[y][(k+span)*4+c]) for y in ys for c in range(3)))
            lum_controls.append(statistics.mean(abs(lum(data[y],k+span)-lum(data[y],k)) for y in ys))
        p99=sorted(controls)[min(len(controls)-1,math.floor(len(controls)*.99))] if controls else 0
        lum_p99=sorted(lum_controls)[min(len(lum_controls)-1,math.floor(len(lum_controls)*.99))] if lum_controls else 0
        cross=[];native=[];steps=[];native_steps=[]
        for y in ys:
            k=min(band-radius-2,max(radius+1,path[y]))
            a,b=k-radius-1,k+radius+1
            cross.extend(abs(data[y][a*4+c]-data[y][b*4+c]) for c in range(3))
            native.extend((abs(source[y][a*4+c]-source[y][b*4+c])+abs(source[y][(length+a)*4+c]-source[y][(length+b)*4+c]))/2 for c in range(3))
            steps.append(lum(data[y],b)-lum(data[y],a))
            native_steps.append((abs(lum(source[y],b)-lum(source[y],a))+abs(lum(source[y],length+b)-lum(source[y],length+a)))/2)
        jump=statistics.mean(cross);baseline=statistics.mean(native)
        step=statistics.mean(map(abs,steps));signed_step=abs(statistics.mean(steps));native_step=statistics.mean(native_steps)
        records.append({'rows':[y0,ys.stop], 'cross_mae':round(jump,6),'interior_p99':round(p99,6),
                        'source_mae':round(baseline,6),'luminance_step':round(step,6),'signed_luminance_step':round(signed_step,6),
                        'luminance_p99':round(lum_p99,6),'source_luminance':round(native_step,6),
                        'pass':jump<=max(1,p99) and jump<=max(3,baseline*1.5+1)
                        and step<=max(1,lum_p99) and step<=max(3,native_step*1.5+1)})
    return records


def narrow_mirror(data):
    length=len(data[0])//4
    result=[]
    def diff(a,b):
        return statistics.mean(abs(row[a*4+c]-row[b*4+c]) for row in data for c in range(3))
    for width in (3,5,8,12):
        if length<4*width+4:continue
        mirror=statistics.mean(diff(k,length-1-k) for k in range(1,width+1))
        controls=[statistics.mean(diff(center-k-1,center+k) for k in range(1,width+1))
                  for center in (length//3,length//2,2*length//3)]
        control=statistics.median(controls)
        result.append({'width':width,'mirror':mirror,'control':control,'ratio':mirror/control if control else 1})
    return result
