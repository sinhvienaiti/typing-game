export type MusicPlaybackMode = "auto-next" | "shuffle" | "repeat-one";

export type LocalMusicTrack = {
  id: string;
  title: string;
  source: "local";
  file: string;
};

export type YouTubeMusicTrack = {
  id: string;
  title: string;
  source: "youtube";
  videoId: string;
};

export type MusicTrack = LocalMusicTrack | YouTubeMusicTrack;

type MusicIndex = {
  version: 1;
  tracks: Array<{
    id: string;
    title: string;
    file: string;
  }>;
};

type StoredMusicState = {
  selectedId: string;
  volume: number;
  playbackMode: MusicPlaybackMode;
  playbackModeVersion: 2;
  duckingEnabled: boolean;
  duckingVolume: number;
  youtubeTracks: YouTubeMusicTrack[];
};

type YouTubePlayer = {
  playVideo(): void;
  pauseVideo(): void;
  seekTo(seconds: number, allowSeekAhead: boolean): void;
  setVolume(volume: number): void;
  getPlayerState(): number;
  destroy(): void;
};

declare global {
  interface Window {
    YT?: {
      Player: new (
        element: HTMLElement,
        options: {
          videoId: string;
          playerVars?: Record<string, string | number>;
          events?: {
            onReady?: () => void;
            onStateChange?: (event: { data: number }) => void;
            onError?: () => void;
          };
        },
      ) => YouTubePlayer;
      PlayerState: {
        ENDED: number;
        PLAYING: number;
        PAUSED: number;
      };
    };
    onYouTubeIframeAPIReady?: () => void;
  }
}

const STORAGE_KEY = "typingGameSharedMusic";
const DEFAULT_VOLUME = 0.32;
const DEFAULT_DUCKING_VOLUME = 0.18;
const DUCK_RELEASE_MS = 160;
const DUCK_ATTACK_MS = 55;
const VOLUME_RELEASE_MS = 220;
let youtubeApiPromise: Promise<void> | null = null;

function loadYouTubeApi(): Promise<void> {
  if (window.YT?.Player !== undefined) return Promise.resolve();
  if (youtubeApiPromise !== null) return youtubeApiPromise;

  youtubeApiPromise = new Promise((resolve, reject) => {
    const previous = window.onYouTubeIframeAPIReady;
    const onReady = (): void => {
      previous?.();
      resolve();
    };
    const onError = (script: HTMLScriptElement): void => {
      script.remove();
      youtubeApiPromise = null;
      if (window.onYouTubeIframeAPIReady === onReady) {
        window.onYouTubeIframeAPIReady = previous;
      }
      reject(new Error("Could not load YouTube Player API"));
    };

    window.onYouTubeIframeAPIReady = onReady;
    const existing = document.querySelector<HTMLScriptElement>(
      'script[src="https://www.youtube.com/iframe_api"]',
    );
    if (existing !== null) {
      existing.addEventListener("error", () => onError(existing), { once: true });
      return;
    }

    const script = document.createElement("script");
    script.src = "https://www.youtube.com/iframe_api";
    script.async = true;
    script.addEventListener("error", () => onError(script), { once: true });
    document.head.append(script);
  });

  return youtubeApiPromise;
}

export function extractYouTubeId(value: string): string | null {
  const trimmed = value.trim();
  if (/^[\w-]{11}$/.test(trimmed)) return trimmed;

  try {
    const url = new URL(trimmed);
    if (url.hostname === "youtu.be") {
      const id = url.pathname.split("/").filter(Boolean)[0];
      return id !== undefined && /^[\w-]{11}$/.test(id) ? id : null;
    }

    if (url.hostname === "youtube.com" || url.hostname.endsWith(".youtube.com")) {
      const direct = url.searchParams.get("v");
      if (direct !== null && /^[\w-]{11}$/.test(direct)) return direct;
      const parts = url.pathname.split("/").filter(Boolean);
      const marker = parts.findIndex((part) =>
        ["embed", "shorts", "live"].includes(part),
      );
      const id = marker >= 0 ? parts[marker + 1] : undefined;
      return id !== undefined && /^[\w-]{11}$/.test(id) ? id : null;
    }
  } catch {
    return null;
  }

  return null;
}

function loadStoredState(): StoredMusicState {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw === null) {
      return {
        selectedId: "",
        volume: DEFAULT_VOLUME,
        playbackMode: "shuffle",
        playbackModeVersion: 2,
        duckingEnabled: true,
        duckingVolume: DEFAULT_DUCKING_VOLUME,
        youtubeTracks: [],
      };
    }

    const data = JSON.parse(raw) as Partial<StoredMusicState>;
    const youtubeTracks = Array.isArray(data.youtubeTracks)
      ? data.youtubeTracks.filter(
          (track): track is YouTubeMusicTrack =>
            track !== null &&
            typeof track === "object" &&
            (track as YouTubeMusicTrack).source === "youtube" &&
            typeof (track as YouTubeMusicTrack).id === "string" &&
            typeof (track as YouTubeMusicTrack).title === "string" &&
            typeof (track as YouTubeMusicTrack).videoId === "string",
        )
      : [];

    return {
      selectedId: typeof data.selectedId === "string" ? data.selectedId : "",
      volume:
        typeof data.volume === "number" && Number.isFinite(data.volume)
          ? Math.min(1, Math.max(0, data.volume))
          : DEFAULT_VOLUME,
      playbackMode:
        data.playbackModeVersion === 2
          ? data.playbackMode === "repeat-one"
            ? "repeat-one"
            : data.playbackMode === "auto-next"
              ? "auto-next"
              : "shuffle"
          : data.playbackMode === "repeat-one"
            ? "repeat-one"
            : "shuffle",
      playbackModeVersion: 2,
      duckingEnabled:
        typeof data.duckingEnabled === "boolean" ? data.duckingEnabled : true,
      duckingVolume:
        typeof data.duckingVolume === "number" && Number.isFinite(data.duckingVolume)
          ? Math.min(1, Math.max(0, data.duckingVolume))
          : DEFAULT_DUCKING_VOLUME,
      youtubeTracks,
    };
  } catch {
    return {
      selectedId: "",
      volume: DEFAULT_VOLUME,
      playbackMode: "shuffle",
      playbackModeVersion: 2,
      duckingEnabled: true,
      duckingVolume: DEFAULT_DUCKING_VOLUME,
      youtubeTracks: [],
    };
  }
}

function saveStoredState(state: StoredMusicState): void {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

function localTrackUrl(file: string): string {
  return `/music/${file
    .split("/")
    .map((part) => encodeURIComponent(part))
    .join("/")}`;
}

export class SharedMusicPlayer {
  readonly element: HTMLElement;

  private readonly toggleButton: HTMLButtonElement;
  private readonly panel: HTMLElement;
  private readonly trackSelect: HTMLSelectElement;
  private readonly playButton: HTMLButtonElement;
  private readonly nextButton: HTMLButtonElement;
  private readonly volumeInput: HTMLInputElement;
  private readonly volumeValue: HTMLOutputElement;
  private readonly playbackModeSelect: HTMLSelectElement;
  private readonly duckingSelect: HTMLSelectElement;
  private readonly duckingVolumeInput: HTMLInputElement;
  private readonly duckingVolumeValue: HTMLOutputElement;
  private readonly status: HTMLElement;
  private readonly youtubeUrlInput: HTMLInputElement;
  private readonly youtubeTitleInput: HTMLInputElement;
  private readonly youtubeHost: HTMLElement;
  private readonly audio = new Audio();

  private localTracks: LocalMusicTrack[] = [];
  private state = loadStoredState();
  private youtubePlayer: YouTubePlayer | null = null;
  private currentTrackId = "";
  private playing = false;
  private desiredPlaying = false;
  private karaokePaused = false;
  private resumeAfterKaraoke = false;
  private speechActive = false;
  private speechReleaseTimer: number | null = null;
  private volumeAnimation: number | null = null;
  private loadToken = 0;
  private shuffleQueue: string[] = [];
  private playbackListener: (playing: boolean) => void = () => {};

  constructor() {
    this.element = document.createElement("div");
    this.element.className = "shared-music";

    this.toggleButton = document.createElement("button");
    this.toggleButton.type = "button";
    this.toggleButton.className = "music-toggle";
    this.toggleButton.setAttribute("aria-expanded", "false");
    this.toggleButton.textContent = "♫ Music";

    this.panel = document.createElement("section");
    this.panel.className = "music-panel hidden";
    this.panel.setAttribute("aria-label", "Background music");

    const heading = document.createElement("div");
    heading.className = "music-heading";
    const headingCopy = document.createElement("div");
    const headingTitle = document.createElement("strong");
    headingTitle.textContent = "Background music";
    const headingSub = document.createElement("span");
    headingSub.textContent = "Shared across games";
    headingCopy.append(headingTitle, headingSub);
    heading.append(headingCopy);

    this.trackSelect = document.createElement("select");
    this.trackSelect.className = "music-track-select";
    this.trackSelect.setAttribute("aria-label", "Background music track");

    const transport = document.createElement("div");
    transport.className = "music-transport";
    this.playButton = document.createElement("button");
    this.playButton.type = "button";
    this.playButton.className = "music-play";
    this.playButton.textContent = "▶ Play";
    this.nextButton = document.createElement("button");
    this.nextButton.type = "button";
    this.nextButton.textContent = "Next →";
    transport.append(this.playButton, this.nextButton);

    const volumeRow = document.createElement("label");
    volumeRow.className = "music-field";
    const volumeLabel = document.createElement("span");
    volumeLabel.textContent = "Music volume";
    this.volumeValue = document.createElement("output");
    this.volumeInput = document.createElement("input");
    this.volumeInput.type = "range";
    this.volumeInput.min = "0";
    this.volumeInput.max = "1";
    this.volumeInput.step = "0.05";
    this.volumeInput.value = String(this.state.volume);
    volumeRow.append(volumeLabel, this.volumeValue, this.volumeInput);

    const settings = document.createElement("details");
    settings.className = "music-settings";
    const settingsSummary = document.createElement("summary");
    settingsSummary.textContent = "Music settings";

    const settingsBody = document.createElement("div");
    settingsBody.className = "music-settings-body";

    const modeLabel = document.createElement("label");
    modeLabel.className = "music-field";
    const modeText = document.createElement("span");
    modeText.textContent = "When a track ends";
    this.playbackModeSelect = document.createElement("select");
    this.playbackModeSelect.innerHTML =
      '<option value="shuffle">Shuffle</option><option value="auto-next">Auto next</option><option value="repeat-one">Repeat one</option>';
    this.playbackModeSelect.value = this.state.playbackMode;
    modeLabel.append(modeText, this.playbackModeSelect);

    const duckingLabel = document.createElement("label");
    duckingLabel.className = "music-field";
    const duckingText = document.createElement("span");
    duckingText.textContent = "Lower music during pronunciation";
    this.duckingSelect = document.createElement("select");
    this.duckingSelect.innerHTML =
      '<option value="true">Enabled</option><option value="false">Disabled</option>';
    this.duckingSelect.value = String(this.state.duckingEnabled);
    duckingLabel.append(duckingText, this.duckingSelect);

    const duckingVolumeLabel = document.createElement("label");
    duckingVolumeLabel.className = "music-field";
    const duckingVolumeText = document.createElement("span");
    duckingVolumeText.textContent = "Pronunciation music level";
    this.duckingVolumeValue = document.createElement("output");
    this.duckingVolumeInput = document.createElement("input");
    this.duckingVolumeInput.type = "range";
    this.duckingVolumeInput.min = "0";
    this.duckingVolumeInput.max = "1";
    this.duckingVolumeInput.step = "0.05";
    this.duckingVolumeInput.value = String(this.state.duckingVolume);
    duckingVolumeLabel.append(
      duckingVolumeText,
      this.duckingVolumeValue,
      this.duckingVolumeInput,
    );

    settingsBody.append(modeLabel, duckingLabel, duckingVolumeLabel);
    settings.append(settingsSummary, settingsBody);

    const youtube = document.createElement("details");
    youtube.className = "music-settings";
    const youtubeSummary = document.createElement("summary");
    youtubeSummary.textContent = "Add YouTube track";
    const youtubeBody = document.createElement("div");
    youtubeBody.className = "music-settings-body";
    this.youtubeUrlInput = document.createElement("input");
    this.youtubeUrlInput.type = "text";
    this.youtubeUrlInput.placeholder = "YouTube URL or video ID";
    this.youtubeUrlInput.autocomplete = "off";
    this.youtubeTitleInput = document.createElement("input");
    this.youtubeTitleInput.type = "text";
    this.youtubeTitleInput.placeholder = "Title (optional)";
    this.youtubeTitleInput.autocomplete = "off";
    const addYoutube = document.createElement("button");
    addYoutube.type = "button";
    addYoutube.textContent = "Add to music list";
    youtubeBody.append(this.youtubeUrlInput, this.youtubeTitleInput, addYoutube);
    youtube.append(youtubeSummary, youtubeBody);

    this.status = document.createElement("div");
    this.status.className = "music-status";
    this.status.setAttribute("role", "status");
    this.status.setAttribute("aria-live", "polite");

    this.youtubeHost = document.createElement("div");
    this.youtubeHost.className = "music-youtube-host";

    this.panel.append(
      heading,
      this.trackSelect,
      transport,
      volumeRow,
      settings,
      youtube,
      this.status,
      this.youtubeHost,
    );
    this.element.append(this.toggleButton, this.panel);

    this.audio.preload = "metadata";
    this.audio.addEventListener("ended", () => this.handleTrackEnded());
    this.audio.addEventListener("error", () => {
      this.playing = false;
      this.desiredPlaying = false;
      this.setStatus("Local track could not be played.");
      this.updatePlayButton();
      this.emitPlaybackChange();
    });

    this.toggleButton.addEventListener("click", () => {
      const open = this.panel.classList.toggle("hidden") === false;
      this.toggleButton.setAttribute("aria-expanded", String(open));
    });

    this.trackSelect.addEventListener("change", () => {
      const wasPlaying = this.desiredPlaying;
      this.state.selectedId = this.trackSelect.value;
      this.shuffleQueue = [];
      saveStoredState(this.state);
      void this.loadSelectedTrack(wasPlaying);
    });

    this.playButton.addEventListener("click", () => {
      void this.togglePlayback();
    });

    this.nextButton.addEventListener("click", () => {
      void this.advanceTrack(true);
    });

    this.volumeInput.addEventListener("input", () => {
      this.state.volume = Number(this.volumeInput.value);
      saveStoredState(this.state);
      this.renderSettingsValues();
      this.applyEffectiveVolume();
    });

    this.playbackModeSelect.addEventListener("change", () => {
      this.state.playbackMode =
        this.playbackModeSelect.value === "repeat-one"
          ? "repeat-one"
          : this.playbackModeSelect.value === "auto-next"
            ? "auto-next"
            : "shuffle";
      this.shuffleQueue = [];
      this.updatePlaybackModeUi();
      saveStoredState(this.state);
    });

    this.duckingSelect.addEventListener("change", () => {
      this.state.duckingEnabled = this.duckingSelect.value === "true";
      saveStoredState(this.state);
      this.applyEffectiveVolume();
    });

    this.duckingVolumeInput.addEventListener("input", () => {
      this.state.duckingVolume = Number(this.duckingVolumeInput.value);
      saveStoredState(this.state);
      this.renderSettingsValues();
      this.applyEffectiveVolume();
    });

    addYoutube.addEventListener("click", () => {
      const videoId = extractYouTubeId(this.youtubeUrlInput.value);
      if (videoId === null) {
        this.setStatus("Enter a valid YouTube URL or 11-character video ID.");
        return;
      }

      const existing = this.state.youtubeTracks.find(
        (track) => track.videoId === videoId,
      );
      if (existing !== undefined) {
        const wasPlaying = this.desiredPlaying;
        this.state.selectedId = existing.id;
        this.shuffleQueue = [];
        this.renderTrackOptions();
        this.trackSelect.value = existing.id;
        saveStoredState(this.state);
        this.setStatus("YouTube track is already in the list.");
        void this.loadSelectedTrack(wasPlaying);
        return;
      }

      const track: YouTubeMusicTrack = {
        id: `youtube:${videoId}`,
        source: "youtube",
        videoId,
        title: this.youtubeTitleInput.value.trim() || `YouTube ${videoId}`,
      };
      this.state.youtubeTracks.push(track);
      this.shuffleQueue = [];
      this.state.selectedId = track.id;
      saveStoredState(this.state);
      this.renderTrackOptions();
      this.trackSelect.value = track.id;
      this.youtubeUrlInput.value = "";
      this.youtubeTitleInput.value = "";
      const wasPlaying = this.desiredPlaying;
      this.setStatus("YouTube track added.");
      void this.loadSelectedTrack(wasPlaying);
    });

    this.renderSettingsValues();
    this.updatePlaybackModeUi();
    this.renderTrackOptions();
    void this.loadLocalTracks();
  }

  onPlaybackChange(listener: (playing: boolean) => void): void {
    this.playbackListener = listener;
  }

  isPlaying(): boolean {
    return this.desiredPlaying && !this.karaokePaused;
  }

  setKaraokeActive(active: boolean): void {
    if (active === this.karaokePaused) return;
    this.karaokePaused = active;

    if (active) {
      this.resumeAfterKaraoke = this.desiredPlaying;
      if (this.playing) this.pauseCurrent(false);
      this.setStatus(
        this.resumeAfterKaraoke
          ? "Paused while Karaoke Typing is active."
          : "Karaoke Typing has audio priority.",
      );
      return;
    }

    const shouldResume = this.resumeAfterKaraoke;
    this.resumeAfterKaraoke = false;
    if (shouldResume) void this.playCurrent();
  }

  setSpeechActive(active: boolean): void {
    if (active) {
      if (this.speechReleaseTimer !== null) {
        window.clearTimeout(this.speechReleaseTimer);
        this.speechReleaseTimer = null;
      }
      this.speechActive = true;
      this.applyEffectiveVolume();
      return;
    }

    if (this.speechReleaseTimer !== null) {
      window.clearTimeout(this.speechReleaseTimer);
    }
    this.speechReleaseTimer = window.setTimeout(() => {
      this.speechReleaseTimer = null;
      this.speechActive = false;
      this.applyEffectiveVolume();
    }, DUCK_RELEASE_MS);
  }

  private async loadLocalTracks(): Promise<void> {
    let response = await fetch("/music/index.local.json", { cache: "no-store" });
    if (!response.ok) {
      response = await fetch("/music/index.json", { cache: "no-store" });
    }

    if (!response.ok) {
      this.setStatus("Local music library is unavailable.");
      return;
    }

    try {
      const data = (await response.json()) as MusicIndex;
      this.localTracks = Array.isArray(data.tracks)
        ? data.tracks
            .filter(
              (track) =>
                typeof track.id === "string" &&
                typeof track.title === "string" &&
                typeof track.file === "string",
            )
            .map((track) => ({
              ...track,
              source: "local" as const,
            }))
        : [];
      this.shuffleQueue = [];
      this.renderTrackOptions();

      const tracks = this.allTracks();
      if (
        this.state.selectedId !== "" &&
        !tracks.some((track) => track.id === this.state.selectedId)
      ) {
        this.state.selectedId = "";
        saveStoredState(this.state);
      }
      this.trackSelect.value = this.state.selectedId;
    } catch {
      this.setStatus("Music index is invalid.");
    }
  }

  private allTracks(): MusicTrack[] {
    return [...this.localTracks, ...this.state.youtubeTracks];
  }

  private renderTrackOptions(): void {
    const current = this.state.selectedId;
    this.trackSelect.replaceChildren();

    const off = document.createElement("option");
    off.value = "";
    off.textContent = "Off";
    this.trackSelect.append(off);

    if (this.localTracks.length > 0) {
      const group = document.createElement("optgroup");
      group.label = "Local";
      for (const track of this.localTracks) {
        const option = document.createElement("option");
        option.value = track.id;
        option.textContent = track.title;
        group.append(option);
      }
      this.trackSelect.append(group);
    }

    if (this.state.youtubeTracks.length > 0) {
      const group = document.createElement("optgroup");
      group.label = "YouTube";
      for (const track of this.state.youtubeTracks) {
        const option = document.createElement("option");
        option.value = track.id;
        option.textContent = track.title;
        group.append(option);
      }
      this.trackSelect.append(group);
    }

    this.trackSelect.value = current;
  }

  private selectedTrack(): MusicTrack | null {
    return (
      this.allTracks().find((track) => track.id === this.state.selectedId) ??
      null
    );
  }

  private async togglePlayback(): Promise<void> {
    if (this.karaokePaused && this.desiredPlaying) {
      this.desiredPlaying = false;
      this.resumeAfterKaraoke = false;
      this.updatePlayButton();
      this.setStatus("Shared music will stay paused after Karaoke.");
      this.emitPlaybackChange();
      return;
    }

    if (this.playing) {
      this.pauseCurrent(true);
      return;
    }
    await this.playCurrent();
  }

  private async playCurrent(): Promise<void> {
    if (this.karaokePaused) {
      this.desiredPlaying = true;
      this.resumeAfterKaraoke = true;
      this.setStatus("Karaoke Typing currently has audio priority.");
      return;
    }

    if (this.selectedTrack() === null) {
      if (this.state.playbackMode !== "shuffle") {
        this.setStatus("Choose a track first.");
        return;
      }

      const randomTrack = this.takeShuffleTrack();
      if (randomTrack === null) {
        this.setStatus("No music tracks are available.");
        return;
      }

      this.state.selectedId = randomTrack.id;
      this.trackSelect.value = randomTrack.id;
      saveStoredState(this.state);
    }

    this.desiredPlaying = true;
    this.emitPlaybackChange();
    const requestedId = this.state.selectedId;
    try {
      if (this.currentTrackId !== requestedId) {
        await this.loadSelectedTrack(false);
      }
      if (this.state.selectedId !== requestedId) return;

      const track = this.selectedTrack();
      if (track === null) return;

      if (track.source === "local") {
        await this.audio.play();
      } else {
        if (this.youtubePlayer === null) {
          throw new Error("YouTube player is not ready");
        }
        this.youtubePlayer.playVideo();
      }
      this.playing = true;
      this.updatePlayButton();
      this.applyEffectiveVolume(false);
      this.setStatus(`Playing: ${track.title}`);
      this.emitPlaybackChange();
    } catch {
      this.playing = false;
      this.desiredPlaying = false;
      this.updatePlayButton();
      this.setStatus("This track could not be played.");
      this.emitPlaybackChange();
    }
  }

  private pauseCurrent(userRequested: boolean): void {
    this.audio.pause();
    this.youtubePlayer?.pauseVideo();
    this.playing = false;
    if (userRequested) this.desiredPlaying = false;
    this.updatePlayButton();
    this.emitPlaybackChange();
  }

  private async loadSelectedTrack(playAfterLoad: boolean): Promise<void> {
    const token = ++this.loadToken;
    this.audio.pause();
    this.audio.removeAttribute("src");
    this.audio.load();
    this.youtubePlayer?.destroy();
    this.youtubePlayer = null;
    this.youtubeHost.replaceChildren();
    this.playing = false;
    this.currentTrackId = "";
    this.emitPlaybackChange();

    const track = this.selectedTrack();
    if (track === null) {
      this.desiredPlaying = false;
      this.updatePlayButton();
      this.setStatus("Background music is off.");
      this.emitPlaybackChange();
      return;
    }

    if (track.source === "local") {
      this.audio.src = localTrackUrl(track.file);
      this.audio.load();
      this.currentTrackId = track.id;
      this.applyEffectiveVolume(false);
      this.setStatus(`Selected: ${track.title}`);
      if (playAfterLoad) await this.playCurrent();
      return;
    }

    this.setStatus("Loading YouTube track…");
    await loadYouTubeApi();
    if (token !== this.loadToken || window.YT?.Player === undefined) return;

    const host = document.createElement("div");
    this.youtubeHost.replaceChildren(host);
    const player = await new Promise<YouTubePlayer>((resolve, reject) => {
      let instance: YouTubePlayer;
      instance = new window.YT!.Player(host, {
        videoId: track.videoId,
        playerVars: {
          autoplay: 0,
          controls: 0,
          rel: 0,
          playsinline: 1,
        },
        events: {
          onReady: () => resolve(instance),
          onStateChange: (event) => {
            if (event.data === window.YT?.PlayerState.ENDED) {
              this.handleTrackEnded();
            } else if (event.data === window.YT?.PlayerState.PLAYING) {
              this.playing = true;
              this.updatePlayButton();
              this.emitPlaybackChange();
            } else if (event.data === window.YT?.PlayerState.PAUSED) {
              this.playing = false;
              this.updatePlayButton();
              this.emitPlaybackChange();
            }
          },
          onError: () => reject(new Error("YouTube playback failed")),
        },
      });
    });

    if (token !== this.loadToken) {
      player.destroy();
      return;
    }

    this.youtubePlayer = player;
    this.currentTrackId = track.id;
    this.applyEffectiveVolume(false);
    this.setStatus(`Selected: ${track.title}`);
    if (playAfterLoad) await this.playCurrent();
  }

  private handleTrackEnded(): void {
    if (!this.desiredPlaying || this.karaokePaused) return;
    if (this.state.playbackMode === "repeat-one") {
      if (this.selectedTrack()?.source === "local") {
        this.audio.currentTime = 0;
        void this.playCurrent();
      } else {
        this.youtubePlayer?.seekTo(0, true);
        this.youtubePlayer?.playVideo();
      }
      return;
    }

    void this.advanceTrack(false);
  }

  private refillShuffleQueue(currentId: string): void {
    const ids = this.allTracks()
      .map((track) => track.id)
      .filter((id) => id !== currentId);

    for (let index = ids.length - 1; index > 0; index -= 1) {
      const swapIndex = Math.floor(Math.random() * (index + 1));
      [ids[index], ids[swapIndex]] = [ids[swapIndex]!, ids[index]!];
    }

    this.shuffleQueue = ids;
  }

  private takeShuffleTrack(): MusicTrack | null {
    const tracks = this.allTracks();
    if (tracks.length === 0) return null;
    if (tracks.length === 1) return tracks[0] ?? null;

    const currentId = this.state.selectedId;
    while (this.shuffleQueue.length > 0) {
      const nextId = this.shuffleQueue.shift();
      if (nextId === undefined || nextId === currentId) continue;
      const track = tracks.find((item) => item.id === nextId);
      if (track !== undefined) return track;
    }

    this.refillShuffleQueue(currentId);
    const nextId = this.shuffleQueue.shift();
    return tracks.find((item) => item.id === nextId) ?? null;
  }

  private async advanceTrack(userRequested: boolean): Promise<void> {
    const tracks = this.allTracks();
    if (tracks.length === 0) {
      this.setStatus("No music tracks are available.");
      return;
    }

    if (this.state.playbackMode === "shuffle") {
      const randomTrack = this.takeShuffleTrack();
      if (randomTrack === null) return;
      this.state.selectedId = randomTrack.id;
    } else {
      const currentIndex = tracks.findIndex(
        (track) => track.id === this.state.selectedId,
      );
      const nextIndex = currentIndex < 0 ? 0 : (currentIndex + 1) % tracks.length;
      this.state.selectedId = tracks[nextIndex]?.id ?? "";
    }

    this.trackSelect.value = this.state.selectedId;
    saveStoredState(this.state);

    const shouldPlay = userRequested ? true : this.desiredPlaying;
    if (userRequested) this.desiredPlaying = true;
    await this.loadSelectedTrack(shouldPlay);
  }

  private effectiveVolume(): number {
    if (!this.state.duckingEnabled || !this.speechActive) {
      return this.state.volume;
    }
    return this.state.volume * this.state.duckingVolume;
  }

  private applyEffectiveVolume(smooth = true): void {
    const target = Math.min(1, Math.max(0, this.effectiveVolume()));
    if (this.volumeAnimation !== null) {
      cancelAnimationFrame(this.volumeAnimation);
      this.volumeAnimation = null;
    }

    if (!smooth) {
      this.audio.volume = target;
      this.youtubePlayer?.setVolume(Math.round(target * 100));
      return;
    }

    const start = this.audio.volume;
    const startedAt = performance.now();
    const fadeMs = target < start ? DUCK_ATTACK_MS : VOLUME_RELEASE_MS;
    const update = (now: number): void => {
      const progress = Math.min(1, (now - startedAt) / fadeMs);
      const volume = start + (target - start) * progress;
      this.audio.volume = Math.min(1, Math.max(0, volume));
      this.youtubePlayer?.setVolume(Math.round(volume * 100));
      if (progress < 1) {
        this.volumeAnimation = requestAnimationFrame(update);
      } else {
        this.volumeAnimation = null;
      }
    };
    this.volumeAnimation = requestAnimationFrame(update);
  }

  private updatePlaybackModeUi(): void {
    this.nextButton.textContent =
      this.state.playbackMode === "shuffle" ? "Shuffle →" : "Next →";
  }

  private renderSettingsValues(): void {
    this.volumeValue.value = `${Math.round(this.state.volume * 100)}%`;
    this.duckingVolumeValue.value =
      `${Math.round(this.state.duckingVolume * 100)}%`;
  }

  private updatePlayButton(): void {
    if (this.karaokePaused && this.desiredPlaying) {
      this.playButton.textContent = "■ Don't resume";
    } else {
      this.playButton.textContent = this.playing ? "⏸ Pause" : "▶ Play";
    }
    this.toggleButton.classList.toggle("playing", this.isPlaying());
  }

  private setStatus(message: string): void {
    this.status.textContent = message;
  }

  private emitPlaybackChange(): void {
    this.playbackListener(this.isPlaying());
  }
}
