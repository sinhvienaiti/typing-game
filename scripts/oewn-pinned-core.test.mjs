import test from "node:test";
import assert from "node:assert/strict";
import {parseOewnEntryYaml,parseOewnSynsetYaml} from "./oewn-pinned-core.mjs";

test("entry parser keeps a sense when a relation precedes id",()=>{
  const yaml=`go:
  v:
    form:
    - gone
    - went
    pronunciation:
    - value: ɡoʊ
      variety: US
    sense:
    - also:
      - 'go_on%2:38:00::'
      id: 'go%2:38:00::'
      sent:
      - The children go to the playground
      synset: 01839438-v
    - id: 'go%2:42:00::'
      synset: 02685941-v
`;
  const parsed=parseOewnEntryYaml(yaml,new Set(["go"])).get("go");
  assert.deepEqual(parsed.parts.v.forms,["gone","went"]);
  assert.deepEqual(parsed.parts.v.pronunciations,[{value:"ɡoʊ",variety:"US"}]);
  assert.deepEqual(parsed.parts.v.senses.map(s=>s.senseId),["go%2:38:00::","go%2:42:00::"]);
});
test("synset parser extracts definitions examples members and POS",()=>{
  const yaml=`01839438-v:
  definition:
  - change location; move, travel, or proceed
  example:
  - How fast does your new car go?
  ili: i27001
  members:
  - go
  - move
  partOfSpeech: v
`;
  const record=parseOewnSynsetYaml(yaml,new Set(["01839438-v"])).get("01839438-v");
  assert.equal(record.definitions[0],"change location; move, travel, or proceed");
  assert.equal(record.examples[0],"How fast does your new car go?");
  assert.deepEqual(record.members,["go","move"]);
  assert.equal(record.partOfSpeech,"v");
});
