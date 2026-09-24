export type VocabularyEntry = {
  id: string;
  en: string;
  vi: string;
  ipa: string;
  level: number;
};

export type ReviewOption = {
  id: string;
  label: string;
};

type VocabularyLookup = {
  version: number;
  entries: Record<string, number>;
};

type VocabularyLevel = {
  version: number;
  level: number;
  entries: Array<{
    id: string;
    en: string;
    vi: string;
    ipa: string;
  }>;
};

type TopicIndex = {
  version: number;
  topics: Array<{
    id: string;
    label: string;
    groupLabel: string;
    keys: string[];
  }>;
};

type PartOfSpeechIndex = {
  version: number;
  categories: Array<{
    id: string;
    entries: Array<{ key: string; level: number }>;
  }>;
};

type GrammarIndex = {
  version: number;
  modules: Array<{
    id: string;
    label: string;
    group: string;
  }>;
};

function titleCase(value: string): string {
  return value
    .split(/[-_]/)
    .filter((part) => part !== "")
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");
}

export class ReviewVocabularyRepository {
  #lookupPromise: Promise<VocabularyLookup> | null = null;
  #topicPromise: Promise<TopicIndex> | null = null;
  #posPromise: Promise<PartOfSpeechIndex> | null = null;
  #grammarPromise: Promise<GrammarIndex> | null = null;
  #levelPromises = new Map<number, Promise<VocabularyLevel>>();

  async #json<T>(url: string, label: string): Promise<T> {
    const response = await fetch(url, { cache: "force-cache" });
    if (!response.ok) throw new Error(`Could not load ${label}`);
    return (await response.json()) as T;
  }

  async #lookup(): Promise<VocabularyLookup> {
    this.#lookupPromise ??= this.#json<VocabularyLookup>(
      "/vocabulary/lookup.json",
      "vocabulary lookup",
    );
    return this.#lookupPromise;
  }

  async #topics(): Promise<TopicIndex> {
    this.#topicPromise ??= this.#json<TopicIndex>(
      "/vocabulary/topics/index.json",
      "topic index",
    );
    return this.#topicPromise;
  }

  async #partsOfSpeech(): Promise<PartOfSpeechIndex> {
    this.#posPromise ??= this.#json<PartOfSpeechIndex>(
      "/vocabulary/parts-of-speech/index.json",
      "word-type index",
    );
    return this.#posPromise;
  }

  async #grammar(): Promise<GrammarIndex> {
    this.#grammarPromise ??= this.#json<GrammarIndex>(
      "/vocabulary/grammar/index.json",
      "grammar index",
    );
    return this.#grammarPromise;
  }

  async #level(level: number): Promise<VocabularyLevel> {
    const cached = this.#levelPromises.get(level);
    if (cached !== undefined) return cached;

    const promise = this.#json<VocabularyLevel>(
      `/vocabulary/levels/${String(level).padStart(3, "0")}.json`,
      `vocabulary level ${level}`,
    ).catch((error) => {
      this.#levelPromises.delete(level);
      throw error;
    });

    this.#levelPromises.set(level, promise);
    return promise;
  }

  async topicOptions(): Promise<ReviewOption[]> {
    const index = await this.#topics();
    return index.topics.map((topic) => ({
      id: topic.id,
      label: `${topic.groupLabel} · ${topic.label}`,
    }));
  }

  async wordTypeOptions(): Promise<ReviewOption[]> {
    const index = await this.#partsOfSpeech();
    return index.categories.map((category) => ({
      id: category.id,
      label: titleCase(category.id),
    }));
  }

  async grammarOptions(): Promise<ReviewOption[]> {
    const index = await this.#grammar();
    return index.modules.map((module) => ({
      id: module.id,
      label: module.label,
    }));
  }

  async filterLearnedKeys(
    keys: string[],
    filters: {
      topicId?: string;
      wordTypeId?: string;
      level?: number;
    },
  ): Promise<Set<string>> {
    let selected = new Set(keys);

    if (filters.level !== undefined) {
      const lookup = await this.#lookup();
      selected = new Set(
        [...selected].filter(
          (key) => lookup.entries[key] === filters.level,
        ),
      );
    }

    if (filters.topicId !== undefined) {
      const topics = await this.#topics();
      const topic = topics.topics.find((item) => item.id === filters.topicId);
      const allowed = new Set(topic?.keys ?? []);
      selected = new Set([...selected].filter((key) => allowed.has(key)));
    }

    if (filters.wordTypeId !== undefined) {
      const pos = await this.#partsOfSpeech();
      const category = pos.categories.find(
        (item) => item.id === filters.wordTypeId,
      );
      const allowed = new Set(
        (category?.entries ?? []).map((entry) => entry.key),
      );
      selected = new Set([...selected].filter((key) => allowed.has(key)));
    }

    return selected;
  }

  async getMany(keys: string[]): Promise<Map<string, VocabularyEntry>> {
    const lookup = await this.#lookup();
    const levels = new Set<number>();
    for (const key of keys) {
      const level = lookup.entries[key];
      if (level !== undefined) levels.add(level);
    }

    const documents = await Promise.all(
      [...levels].sort((a, b) => a - b).map((level) => this.#level(level)),
    );
    const requested = new Set(keys);
    const result = new Map<string, VocabularyEntry>();

    for (const document of documents) {
      for (const entry of document.entries) {
        const key = entry.en
          .normalize("NFKC")
          .trim()
          .replace(/\s+/g, " ")
          .toLowerCase();
        if (!requested.has(key)) continue;
        result.set(key, { ...entry, level: document.level });
      }
    }

    return result;
  }

  async searchLearnedKeys(
    keys: string[],
    search: string,
  ): Promise<Set<string>> {
    const term = search.normalize("NFKC").trim().toLocaleLowerCase();
    if (term === "") return new Set(keys);

    const matches = new Set(
      keys.filter((key) => key.toLocaleLowerCase().includes(term)),
    );

    const entries = await this.getMany(keys);
    for (const [key, entry] of entries) {
      if (
        entry.en.toLocaleLowerCase().includes(term) ||
        entry.vi.toLocaleLowerCase().includes(term)
      ) {
        matches.add(key);
      }
    }

    return matches;
  }
}
