function leadingSpaces(line) {
  const match=/^ */.exec(line);
  return match?match[0].length:0;
}
function scalar(raw) {
  const value=String(raw??"").trim();
  if (value.length>=2&&value.startsWith("'")&&value.endsWith("'")) return value.slice(1,-1).replace(/''/g,"'");
  if (value.length>=2&&value.startsWith('"')&&value.endsWith('"')) {
    try { return JSON.parse(value); } catch {}
    return value.slice(1,-1);
  }
  return value;
}
export function normalizeOewnLemma(value) {
  return String(value).normalize("NFKC").trim().replace(/\s+/g," ").toLocaleLowerCase("en-US");
}
export function parseOewnEntryYaml(content,targetKeys) {
  const wanted=targetKeys instanceof Set?targetKeys:new Set(targetKeys??[]);
  const result=new Map();
  let lemma=null,pos=null,section=null,currentPronunciation=null,currentSense=null;
  function currentPart() {
    if (!lemma||!pos) return null;
    const key=normalizeOewnLemma(lemma);
    if (!wanted.has(key)) return null;
    let record=result.get(key);
    if (!record) { record={headword:lemma,parts:{}}; result.set(key,record); }
    if (!record.parts[pos]) record.parts[pos]={forms:[],pronunciations:[],senses:[]};
    return record.parts[pos];
  }
  for (const line of String(content).split(/\r?\n/)) {
    const indent=leadingSpaces(line);
    if (indent===0&&line.trim().endsWith(":")&&line.trim()!==":") {
      lemma=scalar(line.trim().slice(0,-1)); pos=null; section=null; currentPronunciation=null; currentSense=null; continue;
    }
    const posMatch=/^  ([nvars]):\s*$/.exec(line);
    if (posMatch) { pos=posMatch[1]; section=null; currentPronunciation=null; currentSense=null; currentPart(); continue; }
    if (!currentPart()) continue;
    const sectionMatch=/^    (form|pronunciation|sense):\s*$/.exec(line);
    if (sectionMatch) { section=sectionMatch[1]; currentPronunciation=null; currentSense=null; continue; }
    const part=currentPart();
    if (section==="form") {
      const item=/^    - (.+?)\s*$/.exec(line);
      if (item) { const value=scalar(item[1]); if (value&&!part.forms.includes(value)) part.forms.push(value); }
      else if (indent===4&&!line.startsWith("    - ")) section=null;
      continue;
    }
    if (section==="pronunciation") {
      const item=/^    - value:\s*(.+?)\s*$/.exec(line);
      if (item) { currentPronunciation={value:scalar(item[1]),variety:null}; part.pronunciations.push(currentPronunciation); continue; }
      const variety=/^      variety:\s*(.+?)\s*$/.exec(line);
      if (variety&&currentPronunciation) { currentPronunciation.variety=scalar(variety[1]); continue; }
      if (indent===4&&!line.startsWith("    - ")) { section=null; currentPronunciation=null; }
      continue;
    }
    if (section==="sense") {
      const listItem=/^    -(?:\s+(.*))?$/.exec(line);
      if (listItem) {
        currentSense={senseId:null,synsetId:null,lexFileNumber:null};
        part.senses.push(currentSense);
        const tail=String(listItem[1]??"").trim();
        const directId=/^id:\s*(.+)$/.exec(tail);
        if (directId) {
          currentSense.senseId=scalar(directId[1]);
          const match=/%[1-5]:(\d\d):/.exec(currentSense.senseId);
          currentSense.lexFileNumber=match?Number(match[1]):null;
        }
        continue;
      }
      const id=/^      id:\s*(.+?)\s*$/.exec(line);
      if (id&&currentSense) {
        currentSense.senseId=scalar(id[1]);
        const match=/%[1-5]:(\d\d):/.exec(currentSense.senseId);
        currentSense.lexFileNumber=match?Number(match[1]):null;
        continue;
      }
      const synset=/^      synset:\s*(.+?)\s*$/.exec(line);
      if (synset&&currentSense) { currentSense.synsetId=scalar(synset[1]); continue; }
      if (indent===4&&!line.startsWith("    - ")) { section=null; currentSense=null; }
    }
  }
  for (const record of result.values()) {
    for (const part of Object.values(record.parts)) part.senses=part.senses.filter(sense=>sense.senseId&&sense.synsetId);
  }
  return result;
}
export function parseOewnSynsetYaml(content,targetIds) {
  const wanted=targetIds instanceof Set?targetIds:new Set(targetIds??[]);
  const result=new Map();
  let id=null,section=null;
  for (const line of String(content).split(/\r?\n/)) {
    const indent=leadingSpaces(line);
    if (indent===0&&line.trim().endsWith(":")) {
      id=scalar(line.trim().slice(0,-1)); section=null;
      if (wanted.has(id)&&!result.has(id)) result.set(id,{synsetId:id,definitions:[],examples:[],members:[],ili:null,partOfSpeech:null});
      continue;
    }
    if (!id||!wanted.has(id)) continue;
    const record=result.get(id);
    const listSection=/^  (definition|example|members):\s*$/.exec(line);
    if (listSection) { section=listSection[1]; continue; }
    const ili=/^  ili:\s*(.+?)\s*$/.exec(line);
    if (ili) { record.ili=scalar(ili[1]); section=null; continue; }
    const pos=/^  partOfSpeech:\s*(.+?)\s*$/.exec(line);
    if (pos) { record.partOfSpeech=scalar(pos[1]); section=null; continue; }
    const item=/^  - (.+?)\s*$/.exec(line);
    if (item&&section) {
      const value=scalar(item[1]);
      const key=section==="definition"?"definitions":section==="example"?"examples":"members";
      if (value&&!record[key].includes(value)) record[key].push(value);
      continue;
    }
    if (indent===2&&!line.startsWith("  - ")) section=null;
  }
  return result;
}
export const OEWN_LEXFILE_NAMES=Object.freeze({
  0:"adj.all.yaml",1:"adj.pert.yaml",2:"adv.all.yaml",3:"noun.Tops.yaml",4:"noun.act.yaml",5:"noun.animal.yaml",
  6:"noun.artifact.yaml",7:"noun.attribute.yaml",8:"noun.body.yaml",9:"noun.cognition.yaml",10:"noun.communication.yaml",
  11:"noun.event.yaml",12:"noun.feeling.yaml",13:"noun.food.yaml",14:"noun.group.yaml",15:"noun.location.yaml",
  16:"noun.motive.yaml",17:"noun.object.yaml",18:"noun.person.yaml",19:"noun.phenomenon.yaml",20:"noun.plant.yaml",
  21:"noun.possession.yaml",22:"noun.process.yaml",23:"noun.quantity.yaml",24:"noun.relation.yaml",25:"noun.shape.yaml",
  26:"noun.state.yaml",27:"noun.substance.yaml",28:"noun.time.yaml",29:"verb.body.yaml",30:"verb.change.yaml",
  31:"verb.cognition.yaml",32:"verb.communication.yaml",33:"verb.competition.yaml",34:"verb.consumption.yaml",
  35:"verb.contact.yaml",36:"verb.creation.yaml",37:"verb.emotion.yaml",38:"verb.motion.yaml",39:"verb.perception.yaml",
  40:"verb.possession.yaml",41:"verb.social.yaml",42:"verb.stative.yaml",43:"verb.weather.yaml",44:"adj.ppl.yaml"
});
