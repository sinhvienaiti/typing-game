export const ENGLISH_CONTENT_CAPABILITIES=Object.freeze({
  monkeytype:Object.freeze(["grammar-topic","example-typing","translation","cloze","error-correction","sentence-building","transformation","listening-typing","contextual-usage","collocation","verb-pattern","phrasal-verb","idiom","chunk"]),
  recall:Object.freeze(["vocabulary","collocation","phrasal-verb","chunk","listening-typing","contextual-usage"]),
  shooter:Object.freeze(["vocabulary","collocation","phrasal-verb","chunk","contextual-usage"]),
  karaoke:Object.freeze(["example-typing","dialogue","listening-typing","translation"]),
  space:Object.freeze(["vocabulary","collocation","phrasal-verb","chunk","grammar-challenge","contextual-usage"])
});
export function supportsEnglishActivity(gameId,activity){
  const list=ENGLISH_CONTENT_CAPABILITIES[gameId];
  return Array.isArray(list)&&list.includes(activity);
}
export function listEnglishActivities(gameId){
  return [...(ENGLISH_CONTENT_CAPABILITIES[gameId]??[])];
}
