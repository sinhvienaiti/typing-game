import {
  applyLearningEvidenceEvent,
  createEmptyEvidenceStore,
  LEARNING_EVIDENCE_VERSION,
} from "./evidence-v2.mjs";

export const LEARNING_EVIDENCE_DB_NAME = "typingGameLearningEvidenceV2";
export const LEARNING_EVIDENCE_STORE_NAME = "evidence";
export const LEARNING_EVIDENCE_KEY = "state";

function openDatabase(indexedDB, databaseName, storeName) {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(databaseName, 1);
    request.onupgradeneeded = () => {
      const database = request.result;
      if (!database.objectStoreNames.contains(storeName)) {
        database.createObjectStore(storeName);
      }
    };
    request.onerror = () => reject(request.error ?? new Error("Could not open learning evidence database"));
    request.onsuccess = () => resolve(request.result);
  });
}

function requestResult(request) {
  return new Promise((resolve, reject) => {
    request.onerror = () => reject(request.error ?? new Error("Learning evidence request failed"));
    request.onsuccess = () => resolve(request.result);
  });
}

function transactionDone(transaction) {
  return new Promise((resolve, reject) => {
    transaction.oncomplete = () => resolve();
    transaction.onerror = () => reject(transaction.error ?? new Error("Learning evidence transaction failed"));
    transaction.onabort = () => reject(transaction.error ?? new Error("Learning evidence transaction aborted"));
  });
}

function normalizeStore(raw) {
  if (raw == null || typeof raw !== "object" || raw.version !== LEARNING_EVIDENCE_VERSION) {
    return createEmptyEvidenceStore();
  }
  return structuredClone(raw);
}

export class BrowserLearningEvidenceStore {
  constructor({
    indexedDB = globalThis.indexedDB,
    databaseName = LEARNING_EVIDENCE_DB_NAME,
    storeName = LEARNING_EVIDENCE_STORE_NAME,
  } = {}) {
    this.indexedDB = indexedDB ?? null;
    this.databaseName = databaseName;
    this.storeName = storeName;
    this.databasePromise = null;
    this.operationChain = Promise.resolve();
    this.memoryFallback = null;
  }

  async database() {
    if (this.indexedDB == null) return null;
    this.databasePromise ??= openDatabase(this.indexedDB, this.databaseName, this.storeName);
    return this.databasePromise;
  }

  async load() {
    const db = await this.database();
    if (db == null) {
      return this.memoryFallback ? structuredClone(this.memoryFallback) : createEmptyEvidenceStore();
    }
    const tx = db.transaction(this.storeName, "readonly");
    const raw = await requestResult(tx.objectStore(this.storeName).get(LEARNING_EVIDENCE_KEY));
    await transactionDone(tx);
    return normalizeStore(raw);
  }

  async persist(state) {
    const db = await this.database();
    if (db == null) {
      this.memoryFallback = structuredClone(state);
      return;
    }
    const tx = db.transaction(this.storeName, "readwrite");
    tx.objectStore(this.storeName).put(state, LEARNING_EVIDENCE_KEY);
    await transactionDone(tx);
  }

  enqueue(operation) {
    const task = this.operationChain.catch(() => undefined).then(operation);
    this.operationChain = task.then(() => undefined, () => undefined);
    return task;
  }

  apply(event) {
    return this.enqueue(async () => {
      const current = await this.load();
      const next = applyLearningEvidenceEvent(current, event);
      await this.persist(next);
      return next;
    });
  }

  applyMany(events) {
    return this.enqueue(async () => {
      let next = await this.load();
      for (const ev of events) {
        next = applyLearningEvidenceEvent(next, ev);
      }
      await this.persist(next);
      return next;
    });
  }

  reset() {
    return this.enqueue(async () => {
      const empty = createEmptyEvidenceStore(new Date().toISOString());
      await this.persist(empty);
      return empty;
    });
  }
}
