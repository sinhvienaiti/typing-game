const ROUTES=Object.freeze([
  [/^lex\.en\./,"dictionary"],[/^sense\./,"dictionary"],[/^morph\./,"dictionary"],[/^usage\./,"dictionary"],
  [/^gr\./,"grammar"],[/^sent\./,"sentences"],[/^ex\./,"sentences"],[/^trans\./,"sentences"],[/^dlg\./,"sentences"],[/^err\./,"sentences"],
  [/^col\./,"phrases"],[/^pat\./,"phrases"],[/^pv\./,"phrases"],[/^idiom\./,"phrases"],[/^chunk\./,"phrases"]
]);
export function datasetForEnglishContentId(id){
  const value=String(id??"");
  return ROUTES.find(([pattern])=>pattern.test(value))?.[1]??null;
}
export function createEnglishReviewItemResolver(runtimeLoader){
  if(!runtimeLoader||typeof runtimeLoader.findById!=="function") throw new TypeError("runtimeLoader.findById is required");
  return async function resolveEnglishReviewItem(id){
    const dataset=datasetForEnglishContentId(id);
    if(!dataset) return null;
    const record=await runtimeLoader.findById(dataset,id);
    return record?{dataset,record}:null;
  };
}
