import {
  applyLearningEvent,
  createEmptyLearningProfile,
  migrateLearningProfile,
} from "./core.mjs";

export const LEARNING_DB_NAME = "typingGameLearning";
export const LEARNING_STORE_NAME = "state";
export const LEARNING_PROFILE_KEY = "profile";

function openDatabase(indexedDB, databaseName, storeName) {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(databaseName, 1);
    request.onupgradeneeded = () => {
      const database = request.result;
      if (!database.objectStoreNames.contains(storeName)) database.createObjectStore(storeName);
    };
    request.onerror = () => reject(request.error ?? new Error("Could not open learning database"));
    request.onsuccess = () => resolve(request.result);
  });
}

function requestResult(request) {
  return new Promise((resolve, reject) => {
    request.onerror = () => reject(request.error ?? new Error("Learning database request failed"));
    request.onsuccess = () => resolve(request.result);
  });
}

function transactionDone(transaction) {
  return new Promise((resolve, reject) => {
    transaction.oncomplete = () => resolve();
    transaction.onerror = () => reject(transaction.error ?? new Error("Learning database transaction failed"));
    transaction.onabort = () => reject(transaction.error ?? new Error("Learning database transaction aborted"));
  });
}

export class BrowserLearningProfileStore {
  constructor({ indexedDB = globalThis.indexedDB, databaseName = LEARNING_DB_NAME, storeName = LEARNING_STORE_NAME } = {}) {
    if (indexedDB == null) throw new Error("IndexedDB is not available");
    this.indexedDB = indexedDB;
    this.databaseName = databaseName;
    this.storeName = storeName;
    this.databasePromise = null;
    this.operationChain = Promise.resolve();
  }

  async database() {
    this.databasePromise ??= openDatabase(this.indexedDB, this.databaseName, this.storeName);
    return this.databasePromise;
  }

  async load() {
    const database = await this.database();
    const transaction = database.transaction(this.storeName, "readonly");
    const raw = await requestResult(transaction.objectStore(this.storeName).get(LEARNING_PROFILE_KEY));
    await transactionDone(transaction);
    return raw == null ? createEmptyLearningProfile() : migrateLearningProfile(raw);
  }

  async persist(profile) {
    const database = await this.database();
    const transaction = database.transaction(this.storeName, "readwrite");
    transaction.objectStore(this.storeName).put(profile, LEARNING_PROFILE_KEY);
    await transactionDone(transaction);
  }

  enqueue(operation) {
    const task = this.operationChain.catch(() => undefined).then(operation);
    this.operationChain = task.then(() => undefined, () => undefined);
    return task;
  }

  save(profile) {
    const safeProfile = migrateLearningProfile(profile);
    return this.enqueue(async () => {
      await this.persist(safeProfile);
      return safeProfile;
    });
  }

  apply(event) {
    return this.enqueue(async () => {
      const current = await this.load();
      const next = applyLearningEvent(current, event);
      await this.persist(next);
      return next;
    });
  }
}
