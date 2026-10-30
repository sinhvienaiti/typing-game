export type EnglishCefr = "A1" | "A2" | "B1" | "B2" | "C1" | "C2";
export type EnglishGrammarTopic = { id: string; cefr: EnglishCefr; title: string; objective: string };
export type EnglishTopicCatalog = { schemaVersion: 1; topics: EnglishGrammarTopic[] };
export type EnglishCurriculumLevel = { schemaVersion: 1; cefr: EnglishCefr; topicIds: string[] };
export type EnglishContentFetch = (input: string, init?: RequestInit) => Promise<Pick<Response, "ok" | "status" | "json">>;
export declare function parseEnglishTopicCatalog(value: unknown): EnglishTopicCatalog;
export declare function parseEnglishCurriculumLevel(value: unknown, expectedCefr: EnglishCefr): EnglishCurriculumLevel;
export declare function createEnglishContentClient(options?: { fetcher?: EnglishContentFetch; baseUrl?: string }): {
  loadTopicCatalog(): Promise<EnglishTopicCatalog>;
  loadCurriculumLevel(cefr: EnglishCefr): Promise<EnglishCurriculumLevel>;
  getGrammarTopic(id: string): Promise<EnglishGrammarTopic | null>;
  listGrammarTopics(query?: { cefr?: EnglishCefr; search?: string }): Promise<EnglishGrammarTopic[]>;
  listCurriculumTopics(cefr: EnglishCefr): Promise<EnglishGrammarTopic[]>;
};
