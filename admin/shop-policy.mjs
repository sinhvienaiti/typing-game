export class ShopPolicyValidationError extends Error {}

function fail(message) {
  throw new ShopPolicyValidationError(message);
}

function object(value, path) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) fail(`${path} must be an object.`);
  return value;
}

function exactKeys(value, path, allowed, required = allowed) {
  for (const key of Object.keys(value)) if (!allowed.includes(key)) fail(`${path}.${key} is not authorable.`);
  for (const key of required) if (!Object.hasOwn(value, key)) fail(`${path}.${key} is required.`);
}

function integer(value, path, min, max) {
  if (typeof value !== "number" || !Number.isInteger(value) || value < min || value > max) {
    fail(`${path} must be an integer from ${min} to ${max}.`);
  }
}

function number(value, path, min, max) {
  if (typeof value !== "number" || !Number.isFinite(value) || value < min || value > max) {
    fail(`${path} must be a finite number from ${min} to ${max}.`);
  }
}

function text(value, path, max) {
  if (typeof value !== "string" || value.trim().length === 0 || value.length > max) {
    fail(`${path} must be a non-empty string up to ${max} characters.`);
  }
}

function idArray(value, path, allowed, max = 200, min = 0) {
  if (!Array.isArray(value) || value.length < min || value.length > max) fail(`${path} must be an array with ${min}-${max} entries.`);
  const seen = new Set();
  for (const candidate of value) {
    if (typeof candidate !== "string" || !allowed.includes(candidate)) fail(`${path} contains an unknown id: ${String(candidate)}.`);
    if (seen.has(candidate)) fail(`${path} contains duplicate id: ${candidate}.`);
    seen.add(candidate);
  }
}

function validatePrice(value, path, contract) {
  const price = object(value, path);
  const currencies = contract.currencies;
  exactKeys(price, path, currencies);
  for (const currency of currencies) integer(price[currency], `${path}.${currency}`, contract.constraints.currencyAmount.min, contract.constraints.currencyAmount.max);
}

function validateGeneration(value, contract) {
  const path = "economy.shop.generation";
  const generation = object(value, path);
  exactKeys(generation, path, ["shopTypes", "equipmentGradeBands", "rareItems"]);
  const ids = contract.ids;
  const limits = contract.constraints;

  const shopTypes = object(generation.shopTypes, `${path}.shopTypes`);
  exactKeys(shopTypes, `${path}.shopTypes`, ids.shopTypes);
  for (const type of ids.shopTypes) {
    const rulePath = `${path}.shopTypes.${type}`;
    const rule = object(shopTypes[type], rulePath);
    exactKeys(rule, rulePath, ["itemPool", "itemCount", "itemStock", "equipmentCount", "allowedEquipmentTiers", "equipmentPool"], ["itemPool", "itemCount", "itemStock", "equipmentCount", "allowedEquipmentTiers"]);
    idArray(rule.itemPool, `${rulePath}.itemPool`, ids.itemIds);
    integer(rule.itemCount, `${rulePath}.itemCount`, limits.generatedCount.min, limits.generatedCount.max);
    integer(rule.itemStock, `${rulePath}.itemStock`, limits.stock.min, limits.stock.max);
    integer(rule.equipmentCount, `${rulePath}.equipmentCount`, limits.generatedCount.min, limits.generatedCount.max);
    if (!Array.isArray(rule.allowedEquipmentTiers) || rule.allowedEquipmentTiers.length === 0) fail(`${rulePath}.allowedEquipmentTiers must not be empty.`);
    const tiers = new Set();
    for (const tier of rule.allowedEquipmentTiers) {
      if (!ids.equipmentTiers.includes(tier)) fail(`${rulePath}.allowedEquipmentTiers contains an unknown tier.`);
      if (tiers.has(tier)) fail(`${rulePath}.allowedEquipmentTiers contains a duplicate tier.`);
      tiers.add(tier);
    }
    if (rule.equipmentPool !== undefined) idArray(rule.equipmentPool, `${rulePath}.equipmentPool`, ids.equipmentIds);
  }

  const bandsByType = object(generation.equipmentGradeBands, `${path}.equipmentGradeBands`);
  exactKeys(bandsByType, `${path}.equipmentGradeBands`, ids.shopTypes);
  for (const type of ids.shopTypes) {
    const bands = bandsByType[type];
    if (!Array.isArray(bands) || bands.length === 0 || bands.length > 50) fail(`${path}.equipmentGradeBands.${type} must have 1-50 bands.`);
    let previousStage = 0;
    bands.forEach((candidate, index) => {
      const bandPath = `${path}.equipmentGradeBands.${type}[${index}]`;
      const band = object(candidate, bandPath);
      exactKeys(band, bandPath, ["minStage", "weights"]);
      integer(band.minStage, `${bandPath}.minStage`, limits.stage.min, limits.stage.max);
      if (band.minStage <= previousStage) fail(`${bandPath}.minStage must be strictly ascending.`);
      previousStage = band.minStage;
      const weights = object(band.weights, `${bandPath}.weights`);
      if (Object.keys(weights).length === 0) fail(`${bandPath}.weights must not be empty.`);
      exactKeys(weights, `${bandPath}.weights`, ids.gradeIds, []);
      let total = 0;
      for (const [grade, weight] of Object.entries(weights)) {
        number(weight, `${bandPath}.weights.${grade}`, limits.gradeWeight.min, limits.gradeWeight.max);
        total += weight;
      }
      if (!(total > 0)) fail(`${bandPath}.weights must total more than zero.`);
    });
  }

  if (!Array.isArray(generation.rareItems) || generation.rareItems.length > ids.itemIds.length) fail(`${path}.rareItems is invalid.`);
  const rareIds = new Set();
  generation.rareItems.forEach((candidate, index) => {
    const rulePath = `${path}.rareItems[${index}]`;
    const rule = object(candidate, rulePath);
    exactKeys(rule, rulePath, ["itemId", "baseChanceByShopType", "luckMultiplierPerPoint", "maxMultiplier"]);
    if (!ids.itemIds.includes(rule.itemId)) fail(`${rulePath}.itemId is unknown.`);
    if (rareIds.has(rule.itemId)) fail(`${rulePath}.itemId is duplicated.`);
    rareIds.add(rule.itemId);
    const chances = object(rule.baseChanceByShopType, `${rulePath}.baseChanceByShopType`);
    exactKeys(chances, `${rulePath}.baseChanceByShopType`, ids.shopTypes, []);
    for (const [type, chance] of Object.entries(chances)) number(chance, `${rulePath}.baseChanceByShopType.${type}`, 0, 1);
    number(rule.luckMultiplierPerPoint, `${rulePath}.luckMultiplierPerPoint`, 0, 1);
    number(rule.maxMultiplier, `${rulePath}.maxMultiplier`, 0, 100);
  });
}

function validatePricing(value, contract) {
  const path = "economy.shop.pricing";
  const pricing = object(value, path);
  exactKeys(pricing, path, ["itemGradePrices", "equipmentGradePrices", "equipmentTierAdjustments"]);
  for (const tableName of ["itemGradePrices", "equipmentGradePrices"]) {
    const table = object(pricing[tableName], `${path}.${tableName}`);
    exactKeys(table, `${path}.${tableName}`, contract.ids.shopTypes);
    for (const type of contract.ids.shopTypes) {
      const grades = object(table[type], `${path}.${tableName}.${type}`);
      exactKeys(grades, `${path}.${tableName}.${type}`, contract.ids.gradeIds);
      for (const grade of contract.ids.gradeIds) validatePrice(grades[grade], `${path}.${tableName}.${type}.${grade}`, contract);
    }
  }
  const adjustments = object(pricing.equipmentTierAdjustments, `${path}.equipmentTierAdjustments`);
  exactKeys(adjustments, `${path}.equipmentTierAdjustments`, contract.ids.equipmentTiers.map(String));
  for (const tier of contract.ids.equipmentTiers) {
    const adjustmentPath = `${path}.equipmentTierAdjustments.${tier}`;
    const adjustment = object(adjustments[tier], adjustmentPath);
    exactKeys(adjustment, adjustmentPath, ["creditsMultiplier", "alloyMultiplier", "tier3StarCrystalBonusWhenPriced"]);
    number(adjustment.creditsMultiplier, `${adjustmentPath}.creditsMultiplier`, 0, 100);
    number(adjustment.alloyMultiplier, `${adjustmentPath}.alloyMultiplier`, 0, 100);
    integer(adjustment.tier3StarCrystalBonusWhenPriced, `${adjustmentPath}.tier3StarCrystalBonusWhenPriced`, 0, contract.constraints.currencyAmount.max);
  }
}

function validateAvailability(value, contract) {
  const path = "economy.shop.availability";
  const availability = object(value, path);
  exactKeys(availability, path, contract.ids.shopTypes);
  for (const type of contract.ids.shopTypes) {
    const rulePath = `${path}.${type}`;
    const rule = object(availability[type], rulePath);
    if (rule.kind === "always") exactKeys(rule, rulePath, ["kind"]);
    else if (rule.kind === "discovery") {
      exactKeys(rule, rulePath, ["kind", "discoveryId"]);
      if (!contract.ids.discoveryIds.includes(rule.discoveryId)) fail(`${rulePath}.discoveryId is unknown.`);
    } else if (rule.kind === "seeded-chance") {
      exactKeys(rule, rulePath, ["kind", "baseChance", "luckPerPoint", "maxChance"]);
      number(rule.baseChance, `${rulePath}.baseChance`, 0, 1);
      number(rule.luckPerPoint, `${rulePath}.luckPerPoint`, 0, 1);
      number(rule.maxChance, `${rulePath}.maxChance`, 0, 1);
      if (rule.baseChance > rule.maxChance) fail(`${rulePath}.baseChance cannot exceed maxChance.`);
    } else fail(`${rulePath}.kind is unsupported.`);
  }
}

function validateOfferPriceMap(value, path, contract, byGrade) {
  const byType = object(value, path);
  exactKeys(byType, path, contract.ids.shopTypes, []);
  for (const [type, candidate] of Object.entries(byType)) {
    if (!byGrade) validatePrice(candidate, `${path}.${type}`, contract);
    else {
      const grades = object(candidate, `${path}.${type}`);
      exactKeys(grades, `${path}.${type}`, contract.ids.gradeIds, []);
      for (const [grade, price] of Object.entries(grades)) validatePrice(price, `${path}.${type}.${grade}`, contract);
    }
  }
}

function validateOffers(value, contract) {
  const path = "economy.shop.offers";
  const offers = object(value, path);
  exactKeys(offers, path, ["items", "equipment"]);
  const items = object(offers.items, `${path}.items`);
  exactKeys(items, `${path}.items`, contract.ids.itemIds, []);
  for (const [id, candidate] of Object.entries(items)) {
    const offerPath = `${path}.items.${id}`;
    const offer = object(candidate, offerPath);
    exactKeys(offer, offerPath, ["enabled", "shopTypes", "stockByShopType", "priceByShopType", "compareAtPriceByShopType", "badge"], []);
    if (offer.enabled !== undefined && typeof offer.enabled !== "boolean") fail(`${offerPath}.enabled must be boolean.`);
    if (offer.shopTypes !== undefined) idArray(offer.shopTypes, `${offerPath}.shopTypes`, contract.ids.shopTypes);
    if (offer.stockByShopType !== undefined) {
      const stock = object(offer.stockByShopType, `${offerPath}.stockByShopType`);
      exactKeys(stock, `${offerPath}.stockByShopType`, contract.ids.shopTypes, []);
      for (const [type, amount] of Object.entries(stock)) integer(amount, `${offerPath}.stockByShopType.${type}`, contract.constraints.stock.min, contract.constraints.stock.max);
    }
    if (offer.priceByShopType !== undefined) validateOfferPriceMap(offer.priceByShopType, `${offerPath}.priceByShopType`, contract, false);
    if (offer.compareAtPriceByShopType !== undefined) validateOfferPriceMap(offer.compareAtPriceByShopType, `${offerPath}.compareAtPriceByShopType`, contract, false);
    if (offer.badge !== undefined && offer.badge !== null) text(offer.badge, `${offerPath}.badge`, contract.constraints.badgeMax);
  }
  const equipment = object(offers.equipment, `${path}.equipment`);
  exactKeys(equipment, `${path}.equipment`, contract.ids.equipmentIds, []);
  for (const [id, candidate] of Object.entries(equipment)) {
    const offerPath = `${path}.equipment.${id}`;
    const offer = object(candidate, offerPath);
    exactKeys(offer, offerPath, ["enabled", "shopTypes", "priceByShopTypeAndGrade", "compareAtPriceByShopTypeAndGrade", "badge"], []);
    if (offer.enabled !== undefined && typeof offer.enabled !== "boolean") fail(`${offerPath}.enabled must be boolean.`);
    if (offer.shopTypes !== undefined) idArray(offer.shopTypes, `${offerPath}.shopTypes`, contract.ids.shopTypes);
    if (offer.priceByShopTypeAndGrade !== undefined) validateOfferPriceMap(offer.priceByShopTypeAndGrade, `${offerPath}.priceByShopTypeAndGrade`, contract, true);
    if (offer.compareAtPriceByShopTypeAndGrade !== undefined) validateOfferPriceMap(offer.compareAtPriceByShopTypeAndGrade, `${offerPath}.compareAtPriceByShopTypeAndGrade`, contract, true);
    if (offer.badge !== undefined && offer.badge !== null) text(offer.badge, `${offerPath}.badge`, contract.constraints.badgeMax);
  }
}

function numericRecord(value, path, allowedKeys, min, max, requireAll = true) {
  const record = object(value, path);
  exactKeys(record, path, allowedKeys, requireAll ? allowedKeys : []);
  for (const [key, candidate] of Object.entries(record)) number(candidate, `${path}.${key}`, min, max);
}

function validateUpgradeCost(value, path, contract) {
  const cost = object(value, path);
  exactKeys(cost, path, ["credits", "alloy", "starCrystal", "quantumCore", "requiredStage"]);
  for (const currency of contract.currencies) integer(cost[currency], `${path}.${currency}`, 0, contract.constraints.currencyAmount.max);
  integer(cost.requiredStage, `${path}.requiredStage`, contract.constraints.stage.min, contract.constraints.stage.max);
}

function validateServices(value, contract) {
  const path = "economy.shop.services";
  const services = object(value, path);
  exactKeys(services, path, ["repairPack", "equipmentEnhancement", "equipmentEvolution", "affixes", "dismantle", "progressionOwner"]);
  if (services.progressionOwner !== "progression/upgrades") fail(`${path}.progressionOwner must remain progression/upgrades.`);
  const repair = object(services.repairPack, `${path}.repairPack`);
  exactKeys(repair, `${path}.repairPack`, ["credits", "alloy"]);
  integer(repair.credits, `${path}.repairPack.credits`, 0, contract.constraints.currencyAmount.max);
  integer(repair.alloy, `${path}.repairPack.alloy`, 0, contract.constraints.currencyAmount.max);

  const enhancement = object(services.equipmentEnhancement, `${path}.equipmentEnhancement`);
  exactKeys(enhancement, `${path}.equipmentEnhancement`, ["gradeCreditMultiplier", "gradeAlloyBase", "creditBase", "creditPerEnhancement", "maxEnhancement"]);
  numericRecord(enhancement.gradeCreditMultiplier, `${path}.equipmentEnhancement.gradeCreditMultiplier`, contract.ids.gradeIds, 0, 100);
  numericRecord(enhancement.gradeAlloyBase, `${path}.equipmentEnhancement.gradeAlloyBase`, contract.ids.gradeIds, 0, contract.constraints.currencyAmount.max);
  integer(enhancement.creditBase, `${path}.equipmentEnhancement.creditBase`, 0, contract.constraints.currencyAmount.max);
  integer(enhancement.creditPerEnhancement, `${path}.equipmentEnhancement.creditPerEnhancement`, 0, contract.constraints.currencyAmount.max);
  integer(enhancement.maxEnhancement, `${path}.equipmentEnhancement.maxEnhancement`, 0, 100);

  const evolution = object(services.equipmentEvolution, `${path}.equipmentEvolution`);
  exactKeys(evolution, `${path}.equipmentEvolution`, contract.ids.gradeIds, []);
  for (const [grade, cost] of Object.entries(evolution)) validateUpgradeCost(cost, `${path}.equipmentEvolution.${grade}`, contract);

  const affixes = object(services.affixes, `${path}.affixes`);
  exactKeys(affixes, `${path}.affixes`, ["addCreditsBase", "rerollCreditsBase", "addAlloyBase", "rerollAlloyBase", "gradeFactor", "goldStarCrystal", "diamondStarCrystal", "requiredStage"]);
  for (const key of ["addCreditsBase", "rerollCreditsBase", "addAlloyBase", "rerollAlloyBase"]) integer(affixes[key], `${path}.affixes.${key}`, 0, contract.constraints.currencyAmount.max);
  numericRecord(affixes.gradeFactor, `${path}.affixes.gradeFactor`, contract.ids.gradeIds, 0, 100, false);
  numericRecord(affixes.requiredStage, `${path}.affixes.requiredStage`, contract.ids.gradeIds, 1, 1000, false);
  for (const key of ["goldStarCrystal", "diamondStarCrystal"]) {
    const crystal = object(affixes[key], `${path}.affixes.${key}`);
    exactKeys(crystal, `${path}.affixes.${key}`, ["add", "reroll"]);
    integer(crystal.add, `${path}.affixes.${key}.add`, 0, contract.constraints.currencyAmount.max);
    integer(crystal.reroll, `${path}.affixes.${key}.reroll`, 0, contract.constraints.currencyAmount.max);
  }

  const dismantle = object(services.dismantle, `${path}.dismantle`);
  exactKeys(dismantle, `${path}.dismantle`, ["alloyByGrade", "enhancementAlloyDivisor", "starCrystalByGrade"]);
  numericRecord(dismantle.alloyByGrade, `${path}.dismantle.alloyByGrade`, contract.ids.gradeIds, 0, contract.constraints.currencyAmount.max);
  numericRecord(dismantle.starCrystalByGrade, `${path}.dismantle.starCrystalByGrade`, contract.ids.gradeIds, 0, contract.constraints.currencyAmount.max, false);
  number(dismantle.enhancementAlloyDivisor, `${path}.dismantle.enhancementAlloyDivisor`, 0.000001, 1000);
}

export function validateShopPolicy(policy, contract) {
  if (!contract?.ids?.shopTypes?.length || !contract?.constraints) fail("Child Shop Admin contract is incomplete.");
  const input = object(policy, "economy.shop");
  exactKeys(input, "economy.shop", ["schemaVersion", "configRevision", "generation", "pricing", "availability", "offers", "services"]);
  if (input.schemaVersion !== contract.schemaVersion) fail(`economy.shop.schemaVersion must equal ${contract.schemaVersion}.`);
  text(input.configRevision, "economy.shop.configRevision", contract.constraints.configRevisionMax);
  validateGeneration(input.generation, contract);
  validatePricing(input.pricing, contract);
  validateAvailability(input.availability, contract);
  validateOffers(input.offers, contract);
  validateServices(input.services, contract);
  return policy;
}
