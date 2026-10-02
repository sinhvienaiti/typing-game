const DEFAULT_BASE="/shared";
const DATASETS=Object.freeze(["dictionary","grammar","sentences","phrases"]);
function cleanBase(value){const trimmed=String(value||DEFAULT_BASE).replace(/\/+$/,"");return trimmed||DEFAULT_BASE;}
function isObject(value){return value!==null&&typeof value==="object"&&!Array.isArray(value);}
export function parseRuntimeManifest(value,expectedDataset){
  if(!isObject(value)||value.schemaVersion!==1||value.dataset!==expectedDataset||!Number.isInteger(value.count)||value.count<0||!Array.isArray(value.shards)) throw new TypeError("Invalid runtime manifest for "+expectedDataset);
  const ids=new Set(),paths=new Set(); let sum=0;
  const shards=value.shards.map(shard=>{
    if(!isObject(shard)||typeof shard.id!=="string"||!shard.id||typeof shard.path!=="string"||!shard.path||!Number.isInteger(shard.count)||shard.count<0) throw new TypeError("Invalid runtime shard for "+expectedDataset);
    if(ids.has(shard.id)||paths.has(shard.path)) throw new TypeError("Duplicate runtime shard in "+expectedDataset);
    ids.add(shard.id);paths.add(shard.path);sum+=shard.count;
    return {id:shard.id,path:shard.path,count:shard.count};
  });
  if(sum!==value.count) throw new TypeError("Runtime manifest count mismatch for "+expectedDataset);
  return {schemaVersion:1,contentVersion:String(value.contentVersion),dataset:expectedDataset,count:value.count,shards};
}
export function createEnglishRuntimeLoader(options={}){
  const fetcher=options.fetcher??fetch,base=cleanBase(options.baseUrl);
  const manifestCache=new Map(),shardCache=new Map();
  async function json(relative){
    const response=await fetcher(base+"/"+relative.replace(/^\/+/,""),{cache:"no-store"});
    if(!response.ok) throw new Error("English runtime request failed: "+response.status+" "+relative);
    return response.json();
  }
  async function loadManifest(dataset){
    if(!DATASETS.includes(dataset)) throw new TypeError("Unsupported English runtime dataset: "+dataset);
    let pending=manifestCache.get(dataset);
    if(!pending){pending=json(dataset+"/manifest.json").then(value=>parseRuntimeManifest(value,dataset));manifestCache.set(dataset,pending);}
    try{return await pending;}catch(error){if(manifestCache.get(dataset)===pending)manifestCache.delete(dataset);throw error;}
  }
  async function loadShard(dataset,shard){
    const key=dataset+":"+shard.path; let pending=shardCache.get(key);
    if(!pending){pending=json(dataset+"/"+shard.path).then(value=>{
      if(!isObject(value)||value.schemaVersion!==1||!Array.isArray(value.records)||value.records.length!==shard.count) throw new TypeError("Invalid English runtime shard: "+key);
      return value.records;
    });shardCache.set(key,pending);}
    try{return await pending;}catch(error){if(shardCache.get(key)===pending)shardCache.delete(key);throw error;}
  }
  async function loadDataset(dataset,{prefix}={}){
    const manifest=await loadManifest(dataset);
    const shards=prefix?manifest.shards.filter(shard=>shard.id.startsWith(prefix)):manifest.shards;
    const groups=await Promise.all(shards.map(shard=>loadShard(dataset,shard)));
    return groups.flat();
  }
  async function findById(dataset,id){
    const records=await loadDataset(dataset);
    return records.find(record=>record?.id===id)??null;
  }
  function clear(){manifestCache.clear();shardCache.clear();}
  return {loadManifest,loadShard,loadDataset,findById,clear};
}
