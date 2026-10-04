import { defineConfig } from "vite";
import { offlineVoskPlugin } from "../scripts/offline-vosk-plugin.mjs";

export default defineConfig({
  plugins: [offlineVoskPlugin()],
  server: {
    host: "127.0.0.1",
    port: 3100,
    strictPort: true,
    allowedHosts: ["typing-game.local"],
    hmr: {
      host: "typing-game.local",
      protocol: "wss",
      clientPort: 443,
    },
  },
});
