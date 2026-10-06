import fs from "node:fs";

const file = "portal/src/admin/space-typing.ts";
let source = fs.readFileSync(file, "utf8");

const importLine = 'import { renderExtendedAdminScreen } from "./space-typing-extended";\n';
if (!source.includes(importLine.trim())) {
  source = source.replace('import "./space-typing-ui.css";\n', 'import "./space-typing-ui.css";\n' + importLine);
}

source = source.replaceAll('phase: "planned"', 'phase: "ready"');
source = source.replace(
  '    return this.renderPlanned(path);',
  '    return renderExtendedAdminScreen(path, this.navigate) ?? this.renderPlanned(path);',
);
source = source.replace('UI REV · A-HOLO-01', 'UI REV · A-HOLO-02');
source = source.replace(
  'Màn này đã có trong Information Architecture nhưng chưa nằm trong milestone UI đầu tiên. Nó sẽ dùng cùng Holo Command component system sau khi 5 màn nền tảng được duyệt.',
  'Route chưa có renderer UI. Đây là fallback guard; toàn bộ route trong master plan phải được render trước khi UI phase được coi là hoàn tất.',
);

fs.writeFileSync(file, source);
