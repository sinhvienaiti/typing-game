from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def replace_once(text,old,new,label):
    count=text.count(old)
    if count!=1:
        raise SystemExit(f"{label}: expected one match, got {count}")
    return text.replace(old,new,1)


def patch_master_plan():
    path=ROOT/"docs/ENGLISH_LEARNING_CONTENT_SYSTEM_MASTER_PLAN.md"
    text=path.read_text(encoding="utf-8")
    replacements=[
        ("Pilot status: **FOURTH CONTROLLED A1 BODY SLICE PUBLISHED LOCALLY; CONTINUING REVIEWED SCALE-UP**.","Pilot status: **A1 RICH GRAMMAR BODY COMPLETE — 45/45 A1 TOPICS REVIEWED AND PUBLISHED**."),
        ("The E05 grammar-body review ledger now overlays **296 digest-bound accepted records**","The E05 grammar-body review ledger now overlays **373 digest-bound accepted records**"),
        ("Published E05 runtime now contains **44 rich grammar topics**: the original 12-topic cross-CEFR pilot plus four controlled A1 body slices with 32 additional topics. Grammar-linked authoring now includes **132 controlled example sentences, 88 exercises and 32 linked common mistakes**.","Published E05 runtime now contains **55 rich grammar topics**: the original 12-topic cross-CEFR pilot plus six controlled A1 body slices with 43 additional topics. This closes A1 at **45/45 rich topic bodies** (2 from the original pilot + 43 from the controlled scale slices). Grammar-linked authoring now includes **165 controlled example sentences, 110 exercises and 43 linked common mistakes**."),
        ("A1 slice 04 adds likes/dislikes with nouns and -ing forms, want/need + to-infinitive, time/place/movement prepositions, adjective position, very/really and basic coordinators. Every scale topic","A1 slice 04 adds likes/dislikes with nouns and -ing forms, want/need + to-infinitive, time/place/movement prepositions, adjective position, very/really and basic coordinators. A1 slice 05 adds because, temporary Present Continuous, Present Simple vs Continuous, was/were, regular/irregular Past Simple, Past Simple negatives/questions and going to intentions. A1 slice 06 closes the level with will, would like and basic word order. Every scale topic"),
        ("The original 72 publication decisions remain intact. The four A1 scale slices add **224 digest-bound publication decisions** (32 topics + 96 examples + 64 exercises + 32 mistakes)","The original 72 publication decisions remain intact. The six A1 scale slices add **301 digest-bound publication decisions** (43 topics + 129 examples + 86 exercises + 43 mistakes)"),
        ("The full 300-topic framework remains the curriculum/taxonomy; **44/300 topics now have reviewed rich runtime bodies**. Further expansion must continue as controlled CEFR slices rather than generating the remaining topics in bulk.","The full 300-topic framework remains the curriculum/taxonomy; **55/300 topics now have reviewed rich runtime bodies**, including **45/45 A1 topics**. Further expansion proceeds from A2 upward as controlled CEFR slices rather than generating the remaining topics in bulk."),
        ("Current published runtime: `shared/dictionary` contains **300 lexemes + 300 senses (600)**; `shared/grammar` contains **44 topics**; `shared/sentences` contains **1,852 records** = **732 examples + 888 exercises + 100 dialogues + 132 reviewed common mistakes**;","Current published runtime: `shared/dictionary` contains **300 lexemes + 300 senses (600)**; `shared/grammar` contains **55 topics**; `shared/sentences` contains **1,918 records** = **765 examples + 910 exercises + 100 dialogues + 143 reviewed common mistakes**;"),
        ("The active controlled manifest now accounts for **4,128 checked-in draft authoring/source records across 37 batches**;","The active controlled manifest now accounts for **4,205 checked-in draft authoring/source records across 39 batches**;"),
        ("grammar topics: **300/300 framework entries**, with **44/300 reviewed rich topic bodies** currently published;","grammar topics: **300/300 framework entries**, with **55/300 reviewed rich topic bodies** currently published, including **45/45 A1 topics**;"),
        ("common mistakes: **132 / 2,000 minimum in published runtime** = the closed 100-record E06 pilot plus 32 reviewed A1 grammar-scale mistakes;","common mistakes: **143 / 2,000 minimum in published runtime** = the closed 100-record E06 pilot plus 43 reviewed A1 grammar-scale mistakes;"),
        ("current published runtime contains **732 examples** (132 E05 grammar-linked + 300 typing-text + 300 Tatoeba);","current published runtime contains **765 examples** (165 E05 grammar-linked + 300 typing-text + 300 Tatoeba);"),
        ("continue grammar-body promotion in small reviewed CEFR slices; the first four A1 scale slices add 32 rich topics and 192 linked sentence-domain records, while E03, E04, E05 and E06 publication still uses digest-bound `draft → published` overlays;","continue grammar-body promotion in small reviewed CEFR slices; A1 is now complete at 45/45 rich topics, with the six A1 scale slices adding 43 rich topics and 258 linked sentence-domain records; continue next with A2 while E03, E04, E05 and E06 publication still uses digest-bound `draft → published` overlays;"),
    ]
    for old,new in replacements:
        text=replace_once(text,old,new,"master plan")
    path.write_text(text,encoding="utf-8")


def patch_e11_snapshot():
    path=ROOT/"scripts/report-english-content-e11-readiness.mjs"
    text=path.read_text(encoding="utf-8")
    for kind in ("grammar/e05-scale-a1-04-topics.json","sentences/e05-scale-a1-04-sentences.json","sentences/e05-scale-a1-04-exercises.json","sentences/e05-scale-a1-04-common-mistakes.json"):
        text=replace_once(text,"content/english/"+kind,"content/english/"+kind.replace("a1-04","a1-06"),"E11 snapshot")
    path.write_text(text,encoding="utf-8")


def main():
    patch_master_plan()
    patch_e11_snapshot()


if __name__=="__main__":
    main()
