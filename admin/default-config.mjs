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
    }
  };
}
