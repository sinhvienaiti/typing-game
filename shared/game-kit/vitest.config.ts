import { defineConfig } from "vitest/config";

// Each module keeps its tests next to it: <module>/*.test.ts.
export default defineConfig({
  test: {
    include: ["*/**/*.test.ts"],
    exclude: ["node_modules/**"],
    environment: "node",
  },
});
