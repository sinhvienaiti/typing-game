// Source: new for the kit: the focus strip's style sheet, injected once per document (no CSS file to sync)
/**
 * Every animated property is transform or opacity (set per frame by the
 * strip); colours change by class, once per key. The hot layer's glow is a
 * static text-shadow under an animated opacity, so a key never repaints a
 * shadow. A game restyles the plate through `plateClass` and the variables.
 */
export const TYPING_FX_CSS = `
.tfx{position:absolute;width:0;height:0;pointer-events:none;z-index:var(--tfx-z,40);font-family:var(--tfx-font);--tfx-size:52px;contain:layout style}
.tfx-stage{position:absolute;left:0;top:0}
.tfx-canvas{position:absolute;left:0;top:0;pointer-events:none}
.tfx-plate{position:absolute;left:0;top:0;opacity:0;border-radius:calc(var(--tfx-size)*.28);background:linear-gradient(180deg,rgba(16,18,30,.74),rgba(8,9,17,.62));box-shadow:0 .18em .6em rgba(0,0,0,.38),inset 0 0 0 1px rgba(255,255,255,.13),inset 0 1px 0 rgba(255,255,255,.1)}
.tfx-rim,.tfx-warn,.tfx-flash{position:absolute;inset:-3px;border-radius:inherit;opacity:0}
.tfx-rim{border:3px solid var(--tfx-hot);box-shadow:0 0 calc(var(--tfx-size)*.45) var(--tfx-accent),inset 0 0 calc(var(--tfx-size)*.22) var(--tfx-accent)}
.tfx-rim.is-gold{border-color:#fff3cf;box-shadow:0 0 calc(var(--tfx-size)*.6) var(--tfx-gold),inset 0 0 calc(var(--tfx-size)*.3) var(--tfx-gold)}
.tfx-warn{border:2px solid var(--tfx-warn);box-shadow:0 0 calc(var(--tfx-size)*.3) var(--tfx-warn)}
.tfx-flash{inset:0;background:radial-gradient(ellipse at 50% 40%,var(--tfx-hot),rgba(255,255,255,0) 72%)}
.tfx-layer{position:absolute;left:0;top:0;width:max-content;display:flex;flex-direction:column;align-items:center;white-space:nowrap;visibility:hidden;transform-origin:50% 40%}
.tfx-layer.is-on{visibility:visible}
.tfx-row{position:relative;font-size:var(--tfx-size);font-weight:var(--tfx-weight,800);line-height:1.2;letter-spacing:.02em;padding:.02em .34em 0}
.tfx-g{position:relative;display:inline-block}
.tfx-g>b{font-weight:inherit}
.tfx-c{display:inline-block;color:var(--tfx-pending);text-shadow:0 .045em 0 rgba(0,0,0,.6),0 0 .22em rgba(0,0,0,.4)}
.tfx-g.is-typed>.tfx-c{color:var(--tfx-typed)}
.tfx-g.is-miss>.tfx-c{color:var(--tfx-warn)}
.tfx-g.is-due::after{content:"";position:absolute;left:14%;right:14%;bottom:.04em;height:.075em;border-radius:.04em;background:var(--tfx-hot);opacity:.9;box-shadow:0 0 .2em var(--tfx-accent)}
.tfx-g.is-miss::after{background:var(--tfx-warn);box-shadow:0 0 .25em var(--tfx-warn)}
.tfx-h,.tfx-a,.tfx-b{position:absolute;left:0;top:0;opacity:0;pointer-events:none}
.tfx-h{color:var(--tfx-hot);text-shadow:0 0 .08em var(--tfx-accent),0 0 .28em var(--tfx-accent),0 0 .55em var(--tfx-accent)}
.tfx-a,.tfx-b{color:var(--tfx-ghost);text-shadow:0 .05em 0 rgba(0,0,0,.55),0 0 .3em rgba(0,0,0,.25)}
.tfx--ghost-hot .tfx-a,.tfx--ghost-hot .tfx-b{color:var(--tfx-hot);text-shadow:0 0 .1em var(--tfx-accent),0 0 .32em var(--tfx-accent)}
.tfx--stamp .tfx-a{text-shadow:0 .05em 0 rgba(0,0,0,.45),0 0 .35em color-mix(in srgb,var(--tfx-accent) 55%,transparent)}
.tfx--stamp .tfx-b{color:rgba(3,2,8,.9);text-shadow:0 0 .1em rgba(0,0,0,.7),0 0 .22em rgba(0,0,0,.45)}
.tfx-mean{font-size:calc(var(--tfx-size)*.36);font-weight:600;color:var(--tfx-meaning);padding:.12em 1em .55em;white-space:normal;max-width:24em;text-align:center;line-height:1.28;text-shadow:0 1px 0 rgba(0,0,0,.65)}
.tfx-mean:empty{display:none}
.tfx-badge{position:absolute;left:0;top:0;opacity:0;font-size:calc(var(--tfx-size)*.4);font-weight:800;letter-spacing:.08em;color:var(--tfx-gold);white-space:nowrap;text-shadow:0 0 .35em rgba(255,196,80,.85),0 .07em 0 rgba(0,0,0,.6)}
.tfx-fly{position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;overflow:visible;z-index:var(--tfx-z,40);font-family:var(--tfx-font)}
.tfx-f{position:absolute;left:0;top:0;display:none;font-size:var(--tfx-size);font-weight:var(--tfx-weight,800);line-height:1;color:var(--tfx-hot);text-shadow:0 0 .12em var(--tfx-accent),0 0 .4em var(--tfx-accent)}
.tfx-f.is-gold{text-shadow:0 0 .12em var(--tfx-gold),0 0 .45em var(--tfx-gold)}
.tfx-hit{position:absolute;left:0;top:0;display:none;width:var(--tfx-size);height:var(--tfx-size);border-radius:50%;border:3px solid var(--tfx-hot);box-shadow:0 0 18px var(--tfx-accent),inset 0 0 12px var(--tfx-accent)}
.tfx-hit.is-gold{box-shadow:0 0 22px var(--tfx-gold),inset 0 0 14px var(--tfx-gold)}
.tfx--host-load .tfx-mean{display:none}
.tfx--load .tfx-b{color:rgba(20,12,12,.85);text-shadow:none}
.tfx--host-load .tfx-g.is-back .tfx-a{color:var(--tfx-typed);text-shadow:0 0 .2em var(--tfx-accent)}
.tfx--host-load .tfx-layer.is-flaw .tfx-h{color:var(--tfx-glass);text-shadow:0 0 .1em var(--tfx-glass),0 0 .3em var(--tfx-accent)}
.tfx-rim.is-crystal{border-color:var(--tfx-glass);box-shadow:0 0 calc(var(--tfx-size)*.6) var(--tfx-glass),inset 0 0 calc(var(--tfx-size)*.3) var(--tfx-accent)}
.tfx-g.is-masked>.tfx-c{color:transparent;text-shadow:none}
.tfx-g.is-hint>.tfx-c{opacity:.62}
.tfx-sweep{position:absolute;left:0;top:var(--tfx-sweep-top,0);width:30%;height:var(--tfx-sweep-h,calc(var(--tfx-size)*.06));border-radius:50%;background:linear-gradient(90deg,transparent,var(--tfx-hot) 42%,var(--tfx-hot) 58%,transparent);opacity:0;pointer-events:none}
.tfx-breathe{position:absolute;inset:var(--tfx-breathe-inset,3px);border-radius:inherit;border:var(--tfx-breathe-w,2px) solid var(--tfx-accent);box-shadow:0 0 calc(var(--tfx-size)*.3) var(--tfx-accent),inset 0 0 calc(var(--tfx-size)*.22) var(--tfx-accent);opacity:0;pointer-events:none}
.tfx-flaw,.tfx-learn,.tfx-stray{position:absolute;left:0;top:0;opacity:0;pointer-events:none;white-space:nowrap}
.tfx-flaw{font-size:calc(var(--tfx-size)*.34);font-weight:800;letter-spacing:.24em;line-height:1;padding:.38em .9em .38em 1.14em;color:var(--tfx-glass);text-shadow:0 0 .35em var(--tfx-accent),0 .06em 0 rgba(0,0,0,.7);background:linear-gradient(180deg,rgba(12,20,28,.92),rgba(5,9,14,.88));border-radius:.3em;box-shadow:0 0 .9em color-mix(in srgb,var(--tfx-accent) 45%,transparent),inset 0 0 0 1px color-mix(in srgb,var(--tfx-glass) 55%,transparent)}
.tfx-learn{font-size:calc(var(--tfx-size)*.36);font-weight:600;line-height:1.25;padding:.32em .95em;width:max-content;max-width:26em;white-space:normal;text-align:center;color:var(--tfx-meaning);background:rgba(5,7,11,.86);border-radius:.35em;text-shadow:0 1px 0 rgba(0,0,0,.65)}
.tfx-learn b{font-weight:800;color:var(--tfx-typed);margin-right:.5em}
.tfx-stray{font-size:var(--tfx-size);font-weight:var(--tfx-weight,800);line-height:1;color:var(--tfx-warn);text-shadow:0 0 .14em var(--tfx-warn),0 .05em 0 rgba(0,0,0,.75),0 0 .4em rgba(0,0,0,.5)}
.tfx-line{position:absolute;left:0;top:0;display:none;font-size:var(--tfx-size);font-weight:var(--tfx-weight,800);line-height:1;white-space:nowrap;letter-spacing:-.02em;color:var(--tfx-hot);text-shadow:0 0 .1em var(--tfx-accent),0 0 .35em var(--tfx-accent)}
.tfx-line.is-flaw{color:var(--tfx-glass);text-shadow:0 0 .1em var(--tfx-glass),0 0 .4em var(--tfx-accent)}
.tfx-rib{position:absolute;left:0;top:0;display:none;width:100px;height:10px;border-radius:5px;transform-origin:0 50%;background:linear-gradient(90deg,color-mix(in srgb,var(--tfx-accent) 70%,transparent),var(--tfx-accent));box-shadow:0 0 6px var(--tfx-accent)}
.tfx-rib.is-thread{background:var(--tfx-hot);box-shadow:none}
.tfx-land{position:absolute;left:0;top:0;display:none;border-radius:3px;background:radial-gradient(ellipse at 50% 50%,var(--tfx-hot) 0 40%,color-mix(in srgb,var(--tfx-accent) 70%,transparent) 72%,transparent);box-shadow:0 0 12px var(--tfx-accent),0 0 3px var(--tfx-hot)}
`;

const STYLE_ID = "typing-fx-css";

/** Adds the sheet to `doc` once. */
export function injectTypingFxCss(doc: Document): void {
  if (doc.getElementById(STYLE_ID) !== null) return;
  const style = doc.createElement("style");
  style.id = STYLE_ID;
  style.textContent = TYPING_FX_CSS;
  doc.head.appendChild(style);
}
