export function createDefaultSpaceTypingConfig(contract) {
  return {
    contractRevision: contract.contractRevision,
    configSchemaVersion: contract.configSchemaVersion,
    worldMusicCatalogSchemaVersion: contract.worldMusicCatalogSchemaVersion,
    audio: {
      profileId: "recommended-v1",
      defaults: {
        master: 1,
        pronunciation: 1,
        music: 0.26,
        ambient: 0.08,
        sfx: 0.5,
        announcer: 0.85
      }
    },
    worldMusic: {
      policyRevision: "b2-three-world-pilot-v1",
      assignments: {}
    },
    system: {
      gameDefaults: {
        defaultMode: "campaign",
        defaultShip: "vanguard",
        difficulty: "normal",
        tutorialEnabled: true,
        pronunciationDefault: true,
        autoSave: true
      },
      network: {
        minimumVersion: "0.1.0",
        autoSaveIntervalSeconds: 30,
        reconnectWindowSeconds: 20,
        offlinePlay: true,
        telemetry: true
      },
      maintenance: {
        enabled: false,
        message: "Scheduled maintenance"
      }
    },
    featureFlags: {
      "voice-mode": { enabled: true, rolloutPercent: 100, scope: "all", risk: "normal" },
      "stamina": { enabled: true, rolloutPercent: 100, scope: "all", risk: "economy" },
      "pvp-reflex": { enabled: true, rolloutPercent: 100, scope: "all", risk: "competitive" },
      "pvp-word-chain": { enabled: true, rolloutPercent: 100, scope: "all", risk: "competitive" },
      "new-boss-renderer": { enabled: true, rolloutPercent: 25, scope: "cohort", risk: "normal" },
      "world-music-v2": { enabled: true, rolloutPercent: 100, scope: "all", risk: "normal" }
    }
  };
}
