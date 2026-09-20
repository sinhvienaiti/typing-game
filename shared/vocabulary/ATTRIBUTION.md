# Shared Vocabulary Data Attribution

The editable vocabulary data in `shared/vocabulary/levels/*.json` and the generated
`index.json` / `lookup.json` artifacts are a modified dataset distributed under
**CC BY-SA 4.0** because the first production batch is derived from thichhoc-dict.

## English-Vietnamese dictionary data

Dữ liệu từ điển: Từ điển Anh–Việt thichhoc.com (thichhoc-dict),
giấy phép CC BY-SA 4.0.
https://github.com/thichhoc-org/thichhoc-dict
Nguồn gốc: WordNet 3.1 (Princeton), CMUdict (CMU), Wiktionary.
Đã chỉnh sửa dữ liệu.

The production batch uses the source as candidate/enrichment data only. Entries are
selected and simplified for this typing curriculum; source data is not copied blindly.

## CEFR reference

Level review uses the CEFR-J Vocabulary Profile as a difficulty reference:

The CEFR-J Wordlist Version 1.5. Compiled by Yukio Tono,
Tokyo University of Foreign Studies.

https://github.com/openlanguageprofiles/olp-en-cefrj

The CEFR-J repository states that the vocabulary profile may be used for research
and commercial purposes without charge when the dataset is properly cited.

## Pronunciation convention

The library standard is **General American IPA**.

The source pipeline primarily derives IPA from CMUdict. Heteronyms are not accepted
blindly: the selected part of speech and intended learner meaning must match the
pronunciation before an entry is promoted into `levels/*.json`.

## Important license scope

The CC BY-SA 4.0 share-alike requirement applies to the derived vocabulary data.
It does not change the license of unrelated application source code that reads the data.
