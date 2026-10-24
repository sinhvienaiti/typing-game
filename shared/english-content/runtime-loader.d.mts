export type EnglishRuntimeDataset="dictionary"|"grammar"|"sentences"|"phrases";
export type EnglishRuntimeShard={id:string;path:string;count:number};
export type EnglishRuntimeManifest={schemaVersion:1;contentVersion:string;dataset:EnglishRuntimeDataset;count:number;shards:EnglishRuntimeShard[]};
export declare function parseRuntimeManifest(value:unknown,expectedDataset:EnglishRuntimeDataset):EnglishRuntimeManifest;
export declare function createEnglishRuntimeLoader(options?:{fetcher?:(input:string,init?:RequestInit)=>Promise<Pick<Response,"ok"|"status"|"json">>;baseUrl?:string}):{
 loadManifest(dataset:EnglishRuntimeDataset):Promise<EnglishRuntimeManifest>;
 loadShard(dataset:EnglishRuntimeDataset,shard:EnglishRuntimeShard):Promise<unknown[]>;
 loadDataset(dataset:EnglishRuntimeDataset,options?:{prefix?:string}):Promise<unknown[]>;
 findById(dataset:EnglishRuntimeDataset,id:string):Promise<any|null>;
 clear():void;
};
