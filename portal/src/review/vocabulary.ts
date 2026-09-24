export type VocabularyEntry = {
  id: string;
  en: string;
  vi: string;
  ipa: string;
  level: number;
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

export class ReviewVocabularyRepository {
  #lookupPromise: Promise<VocabularyLookup> | null = null;
  #levelPromises = new Map<number, Promise<VocabularyLevel>>();

  async #lookup(): Promise<VocabularyLookup> {
    this.#lookupPromise ??= fetch("/vocabulary/lookup.json", {
      cache: "force-cache",
    }).then(async (response) => {
      if (!response.ok) throw new Error("Could not load vocabulary lookup");
      return (await response.json()) as VocabularyLookup;
    });
    return this.#lookupPromise;
  }

  async #level(level: number): Promise<VocabularyLevel> {
    const cached = this.#levelPromises.get(level);
    if (cached !== undefined) return cached;

    const promise = fetch(
      `/vocabulary/levels/${String(level).padStart(3, "0")}.json`,
      { cache: "force-cache" },
    )
      .then(async (response) => {
        if (!response.ok) {
          throw new Error(`Could not load vocabulary level ${level}`);
        }
        return (await response.json()) as VocabularyLevel;
      })
      .catch((error) => {
        this.#levelPromises.delete(level);
        throw error;
      });

    this.#levelPromises.set(level, promise);
    return promise;
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
