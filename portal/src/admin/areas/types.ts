import type { AdminHelpScope } from "../v2/admin-help";
export type NavItem = {
  label: string;
  path: string;
  icon: string;
  description: string;
};

export type NavGroup = {
  id: string;
  label: string;
  description: string;
  items: readonly NavItem[];
  requiredPermission?: string;
};

export type AdminPageContext = { navigate: (path: string) => void; help: AdminHelpScope };
export type AdminArea = { id: string; label: string; base: string; navGroups: readonly NavGroup[]; renderPage: (path: string, context: AdminPageContext) => HTMLElement | null };
