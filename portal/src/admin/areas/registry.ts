import type { AdminArea, AdminPageContext, NavGroup } from "./types";
import { spaceTypingArea } from "./space-typing";
import { sharedArea } from "./shared";
import { renderAdminV2MediaLibrary } from "../v2/media-library";
import { renderAdminV2Roles } from "../v2/roles";

export const ADMIN_AREAS = [sharedArea, spaceTypingArea] as const;
export const ADMINISTRATION: NavGroup = {
  id: "administration", label: "Administration", description: "Shared media and server access for every game.",
  items: [
    { label: "Media Library", path: "/admin/media", icon: "▧", description: "Browse the shared media library and immutable versions." },
    { label: "Roles & Permissions", path: "/admin/roles", icon: "◈", description: "Review server-enforced permissions and role templates." },
  ],
};

export function isAdministrationPath(path: string): boolean {
  return ADMINISTRATION.items.some((item) => item.path === path);
}

/** Administration pages keep the caller's last area (All games when there is none). */
export function areaForPath(path: string, lastAreaId: string | null = null): AdminArea {
  if (isAdministrationPath(path)) return ADMIN_AREAS.find((area) => area.id === lastAreaId) ?? sharedArea;
  return ADMIN_AREAS.find((area) => path === area.base || path.startsWith(`${area.base}/`)) ?? sharedArea;
}

export function renderAdministrationPage(path: string, { help }: AdminPageContext): HTMLElement | null {
  if (path === "/admin/media") return renderAdminV2MediaLibrary(help);
  if (path === "/admin/roles") return renderAdminV2Roles();
  return null;
}
