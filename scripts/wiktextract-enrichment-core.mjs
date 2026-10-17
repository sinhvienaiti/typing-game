export function cleanStrings(values) {
  return [...new Set(
    (Array.isArray(values)?values:[])
      .filter(value=>typeof value==="string"&&value.trim()!=="")
      .map(value=>value.normalize("NFC").trim())
  )];
}

export function parseWiktextractForms(item) {
  const result=[];
  const seen=new Set();
  for (const raw of Array.isArray(item?.forms)?item.forms:[]) {
    if (typeof raw?.form!=="string") continue;
    const form=raw.form.normalize("NFC").trim();
    if (!form||form==="-"||form==="—") continue;
    const tags=cleanStrings([
      ...(Array.isArray(raw.tags)?raw.tags:[]),
      ...(Array.isArray(raw.raw_tags)?raw.raw_tags:[]),
    ]);
    const key=form+"\u0000"+tags.join("\u0000");
    if (seen.has(key)) continue;
    seen.add(key);
    result.push({form,tags});
  }
  return result;
}

export function parseWiktextractSenses(item) {
  const senses=[];
  for (const [index,raw] of (Array.isArray(item?.senses)?item.senses:[]).entries()) {
    const glossesEn=cleanStrings(raw?.glosses);
    const tags=cleanStrings([
      ...(Array.isArray(raw?.tags)?raw.tags:[]),
      ...(Array.isArray(raw?.raw_tags)?raw.raw_tags:[]),
    ]);
    const examples=cleanStrings((Array.isArray(raw?.examples)?raw.examples:[]).flatMap(example=>{
      if (typeof example==="string") return [example];
      if (typeof example?.text==="string") return [example.text];
      return [];
    }));
    if (glossesEn.length===0&&tags.length===0&&examples.length===0) continue;
    senses.push({sourceSenseIndex:index,glossesEn,tags,examples});
  }
  return senses;
}

export function parseWiktextractIpa(item) {
  return cleanStrings((Array.isArray(item?.sounds)?item.sounds:[])
    .flatMap(sound=>typeof sound?.ipa==="string"?[sound.ipa]:[]));
}
