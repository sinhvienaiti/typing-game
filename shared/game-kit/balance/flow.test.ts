// Source: new for the kit: FlowMeter on synthetic timelines (docs/games/BALANCE.md §3)
import { describe, expect, it } from "vitest";
import { FlowMeter, type FlowSnapshot } from "./flow";

const calm: FlowSnapshot = { danger: false, hp: 1, live: 2, capped: false, backlog: 0, busy: true };
const at = (overrides: Partial<FlowSnapshot>): FlowSnapshot => ({ ...calm, ...overrides });

describe("FlowMeter", () => {
  it("measures P, I and O as shares of fed ticks", () => {
    const meter = new FlowMeter();
    meter.feed(at({ danger: true }), 300);
    meter.feed(at({ live: 0, busy: false }), 600);
    meter.feed(at({ backlog: 5 }), 60);
    meter.feed(at({ capped: true }), 60);
    meter.feed(calm, 180);
    const window = meter.window();
    expect(window.ticks).toBe(1200);
    expect([window.p, window.i, window.o]).toEqual([250, 500, 100]);
    const summary = meter.summary("won");
    expect([summary.ticks, summary.p, summary.i, summary.o, summary.s]).toEqual([1200, 250, 500, 100, 1000]);
  });

  it("idle needs no live words and no decision open", () => {
    const meter = new FlowMeter();
    meter.feed(at({ live: 0, busy: true }), 100);
    meter.feed(at({ live: 0, busy: false }), 100);
    expect(meter.window().i).toBe(500);
  });

  it("losing HP counts as pressure for a second", () => {
    const meter = new FlowMeter();
    meter.feed(calm, 100);
    meter.feed(at({ hp: 0.9 }), 1);
    meter.feed(at({ hp: 0.9 }), 199);
    expect(meter.summary("won").p).toBe(Math.round((60 * 1000) / 300));
    expect(meter.window().hpLoss).toBe(100);
  });

  it("two dropped locks within 5 s are overload until the first one is 5 s old", () => {
    const meter = new FlowMeter();
    meter.feed(at({ abandons: 1 }), 100);
    meter.feed(at({ abandons: 1 }), 400);
    // Overload from tick 100 until tick 300 (the first drop is then 300 ticks old).
    expect(meter.summary("won").o).toBe(Math.round((200 * 1000) / 500));
  });

  it("the window holds the last 20 s; the stage holds everything", () => {
    const meter = new FlowMeter();
    meter.feed(at({ danger: true }), 1200);
    meter.feed(calm, 1200);
    expect(meter.window().p).toBe(0);
    expect(meter.summary("won").p).toBe(500);
    meter.feed(at({ danger: true }), 300);
    expect(meter.window().p).toBe(250);
    meter.resetWindow();
    expect(meter.window().ticks).toBe(0);
    meter.feed(at({ danger: true }), 300);
    expect([meter.window().ticks, meter.window().p, meter.summary("won").ticks]).toEqual([300, 1000, 3000]);
  });

  it("one feed of N ticks equals N feeds of one tick", () => {
    const timeline: [FlowSnapshot, number][] = [
      [calm, 250],
      [at({ danger: true, hp: 0.8, kills: [0.5] }), 130],
      [at({ abandons: 2, backlog: 6 }), 77],
      [at({ live: 0, busy: false, hp: 0.25 }), 401],
      [at({ hp: 0.5, kills: [0.62, 0.7], damage: { typed: 30, other: 10 } }), 343],
    ];
    const chunked = new FlowMeter();
    const single = new FlowMeter();
    for (const [snapshot, ticks] of timeline) {
      chunked.feed(snapshot, ticks);
      single.feed(snapshot);
      const rest = { ...snapshot, kills: undefined, abandons: undefined, damage: undefined };
      for (let tick = 1; tick < ticks; tick += 1) single.feed(rest);
    }
    expect(single.state()).toEqual(chunked.state());
    expect(single.summary("won")).toEqual(chunked.summary("won"));
  });

  it("counts a near miss when HP falls under 30 % and comes back, or the stage is won", () => {
    const recovered = new FlowMeter();
    recovered.feed(at({ hp: 0.25 }), 60);
    recovered.feed(at({ hp: 0.45 }), 60);
    recovered.feed(at({ hp: 0.2 }), 60);
    expect(recovered.summary("won").n).toBe(2);
    expect(recovered.summary("lost").n).toBe(1);
    expect(recovered.summary("lost").s).toBe(0);
    const hovering = new FlowMeter();
    hovering.feed(at({ hp: 0.29 }), 60);
    hovering.feed(at({ hp: 0.35 }), 60);
    hovering.feed(at({ hp: 0.28 }), 60);
    expect(hovering.summary("won").n).toBe(1);
    expect(hovering.window().nearDefeat).toBe(true);
    expect(hovering.summary("won").hpMin).toBe(280);
  });

  it("Q is the median path fraction at death; support is the share of damage not typed", () => {
    const meter = new FlowMeter();
    meter.feed(at({ kills: [0.2, 0.9], damage: { typed: 80, other: 20 } }), 10);
    meter.feed(at({ kills: [0.5] }), 10);
    expect(meter.window().q).toBe(500);
    meter.feed(at({ kills: [0.6] }), 10);
    expect(meter.window().q).toBe(550);
    const summary = meter.summary("won");
    expect([summary.kills, summary.q, summary.support]).toEqual([4, 550, 200]);
    expect(new FlowMeter().summary("won").q).toBeNull();
    expect(new FlowMeter().summary("won").support).toBeNull();
  });

  it("ignores empty feeds and clamps odd input", () => {
    const meter = new FlowMeter();
    meter.feed(calm, 0);
    meter.feed(at({ hp: 1.7, kills: [Number.NaN, -1] }), 1);
    expect(meter.ticks).toBe(1);
    expect(meter.summary("won").s).toBe(1000);
    expect(meter.summary("won").q).toBe(0);
  });
});
