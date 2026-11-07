export type EnglishCapabilityGameId="monkeytype"|"recall"|"shooter"|"karaoke"|"space";
export declare const ENGLISH_CONTENT_CAPABILITIES:Readonly<Record<EnglishCapabilityGameId,readonly string[]>>;
export declare function supportsEnglishActivity(gameId:string,activity:string):boolean;
export declare function listEnglishActivities(gameId:string):string[];
