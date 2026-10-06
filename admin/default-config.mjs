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
        credit: 1,
        announcer: 0.85,
        categories: {
          typing: 1,
          combat: 1,
          warnings: 1,
          ui: 1,
          rewards: 1
        }
      }
    },
    worldMusic: {
      policyRevision: "b2-three-world-pilot-v1",
      assignments: {}
    },
    content: {
      ships: {
        configRevision: "ships-admin-v1",
        ships: {}
      },
      equipment: {
        configRevision: "equipment-admin-v1",
        equipment: {}
      },
      skills: {
        configRevision: "skills-admin-v1",
        skills: {}
      }
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
