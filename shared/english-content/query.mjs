const DEFAULT_BASE="/shared";

function cleanBase(value) {
  const trimmed=String(value||DEFAULT_BASE).replace(/\/+$/,"");
  return trimmed||DEFAULT_BASE;
}
function object(value) {
  return value!==null&&typeof value==="object"&&!Array.isArray(value);
}
export function parseEnglishTopicCatalog(value) {
  if (!object(value)||value.schemaVersion!==1||!Array.isArray(value.topics)) throw new TypeError("English topic catalog is invalid");
  const ids=new Set();
  const topics=value.topics.map(topic=>{
    if (!object(topic)||typeof topic.id!=="string"||!/^gr\.(a1|a2|b1|b2|c1|c2)\.[a-z0-9-]+$/.test(topic.id)||
        !["A1","A2","B1","B2","C1","C2"].includes(topic.cefr)||typeof topic.title!=="string"||topic.title.trim()===""||
        typeof topic.objective!=="string"||topic.objective.trim()==="") throw new TypeError("English topic catalog contains an invalid topic");
    if (ids.has(topic.id)) throw new TypeError("English topic catalog contains duplicate topic ids");
    ids.add(topic.id);
    return {id:topic.id,cefr:topic.cefr,title:topic.title,objective:topic.objective};
  });
  return {schemaVersion:1,topics};
}
export function parseEnglishCurriculumLevel(value,expectedCefr) {
  if (!object(value)||value.schemaVersion!==1||value.cefr!==expectedCefr||!Array.isArray(value.topicIds)||value.topicIds.length===0) throw new TypeError("English curriculum level is invalid");
  const ids=value.topicIds.filter(id=>typeof id==="string");
  if (ids.length!==value.topicIds.length||new Set(ids).size!==ids.length) throw new TypeError("English curriculum level topicIds are invalid");
  return {schemaVersion:1,cefr:expectedCefr,topicIds:[...ids]};
}
export function createEnglishContentClient(options={}) {
  const fetcher=options.fetcher??fetch;
  const base=cleanBase(options.baseUrl);
  let topicCatalogPromise=null;
  const levelPromises=new Map();
  async function json(relative) {
    const response=await fetcher(base+"/"+relative.replace(/^\/+/,""),{cache:"no-store"});
    if (!response.ok) throw new Error("English content request failed: "+response.status+" "+relative);
    return response.json();
  }
  async function loadTopicCatalog() {
    topicCatalogPromise??=json("curriculum/topic-catalog.json").then(parseEnglishTopicCatalog);
    try { return await topicCatalogPromise; } catch (error) { topicCatalogPromise=null; throw error; }
  }
  async function loadCurriculumLevel(cefr) {
    if (!["A1","A2","B1","B2","C1","C2"].includes(cefr)) throw new TypeError("Unsupported CEFR level: "+cefr);
    let pending=levelPromises.get(cefr);
    if (!pending) {
      pending=json("curriculum/"+cefr.toLowerCase()+".json").then(value=>parseEnglishCurriculumLevel(value,cefr));
      levelPromises.set(cefr,pending);
    }
    try { return await pending; } catch (error) { if (levelPromises.get(cefr)===pending) levelPromises.delete(cefr); throw error; }
  }
  async function getGrammarTopic(id) {
    const catalog=await loadTopicCatalog();
    return catalog.topics.find(topic=>topic.id===id)??null;
  }
  async function listGrammarTopics(query={}) {
    const catalog=await loadTopicCatalog();
    const search=String(query.search??"").normalize("NFKC").trim().toLocaleLowerCase("en-US");
    return catalog.topics.filter(topic=>
      (query.cefr===undefined||topic.cefr===query.cefr)&&
      (search===""||topic.title.toLocaleLowerCase("en-US").includes(search)||topic.objective.toLocaleLowerCase("en-US").includes(search))
    );
  }
  async function listCurriculumTopics(cefr) {
    const [level,catalog]=await Promise.all([loadCurriculumLevel(cefr),loadTopicCatalog()]);
    const byId=new Map(catalog.topics.map(topic=>[topic.id,topic]));
    return level.topicIds.map(id=>byId.get(id)).filter(Boolean);
  }
  return {loadTopicCatalog,loadCurriculumLevel,getGrammarTopic,listGrammarTopics,listCurriculumTopics};
}
