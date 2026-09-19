import { defineConfig } from "vite";

export default defineConfig({
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
