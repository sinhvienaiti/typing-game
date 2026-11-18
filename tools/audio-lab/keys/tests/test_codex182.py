"""Test riêng phiếu 182: DSP, nhả phím, đo nền, biến thể và nhịp nghe.

Không chạy game hoặc mô hình; tín hiệu nhân tạo chỉ dùng làm fixture test.
"""
import importlib.util
import unittest
from pathlib import Path

import numpy as np

spec = importlib.util.spec_from_file_location('codex182', Path(__file__).resolve().parents[1]/'codex182.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def stroke(noise=0.):
    rng = np.random.default_rng(182)
    x = rng.normal(0, noise, 8640)
    for start, level in [(48,.5),(4000,.18)]:
        t=np.arange(2400)/c.SR
        hit=(np.sin(2*np.pi*270*t)+.25*np.sin(2*np.pi*1700*t)+.3*np.sin(2*np.pi*6000*t))*np.exp(-t/.004)
        hit[:12]*=np.linspace(0,1,12)
        x[start:start+len(hit)]+=hit*level
    return x


class Codex182Tests(unittest.TestCase):
    def test_cleaning_reduces_hiss_preserves_two_events_and_body(self):
        x=stroke(1e-4)
        for pid in c.PROFILES:
            with self.subTest(pid=pid):
                y,meta=c.clean_stroke(x,pid)
                m=c.measures(y,meta['quiet_windows_samples'])
                b=c.measures(x,[[6000,6500]])
                self.assertLess(m['high4k8k_vs_body150_400_db'],b['high4k8k_vs_body150_400_db']-7)
                self.assertLessEqual(m['noise_floor_dbfs'],-70)
                self.assertLessEqual(m['head_ms'],2)
                self.assertLessEqual(m['main_ms'],15)
                self.assertAlmostEqual(m['lufs_m_max'],-27,places=5)
                # Tiếng nhả thật trong fixture phải còn, đúng ~83 ms sau tiếng nhấn.
                trim=meta['trim_samples']
                a=4000-trim
                press=np.sqrt(np.mean(y[48-trim:800-trim]**2))
                release=np.sqrt(np.mean(y[a:a+752]**2))
                self.assertGreater(release/press,.25)
                self.assertLess(release/press,.5)

    def test_causal_chain_has_no_sound_before_input(self):
        x=stroke()
        y,meta=c.clean_stroke(x,'creamy')
        self.assertTrue(np.all(y[:max(0,48-meta['trim_samples'])]==0))

    def test_silence_is_rejected(self):
        with self.assertRaises(ValueError):
            c.clean_stroke(np.zeros(8640),'thock')

    def test_correlation_catches_delayed_and_inverted_copies(self):
        x=stroke()
        delayed=np.pad(x,(120,0))[:len(x)]
        self.assertGreater(c.correlation(x,delayed),.999)
        self.assertGreater(c.correlation(x,-delayed),.999)
        rng=np.random.default_rng(99)
        self.assertLess(c.correlation(x,rng.normal(size=len(x))),.95)

    def test_interstroke_noise_is_measured_not_ignored(self):
        x=stroke()
        x[6500:8200]=.001
        self.assertAlmostEqual(c.measures(x,[[6500,8200]])['noise_floor_dbfs'],-60)

    def test_quiet_release_is_protected_from_expander(self):
        x=stroke()
        x[4000:6400]*=.04
        unprotected,_=c.clean_stroke(x,'dome')
        protected,meta=c.clean_stroke(x,'dome',release_sample=4000)
        a=4000-meta['trim_samples']
        # Upstroke yếu thật vẫn được giữ thay vì bị coi là nền.
        self.assertGreater(np.linalg.norm(protected[a:a+1000]),5*np.linalg.norm(unprotected[a:a+1000]))

    def test_recovery_retains_same_raw_press_release_and_only_extends_single_take(self):
        raw=np.pad(stroke(),(0,c.SR-8640))
        original=raw.copy()
        metadata={'onset':48,'release_onset':4000,'press_end':7000}
        y,release,a,b=c.recover_event(raw,c.SR,metadata,1)
        self.assertEqual((a,b),(0,8920))
        self.assertAlmostEqual(release,4000/48)
        self.assertGreater(np.max(np.abs(y[4000:4500])),.02)
        self.assertGreater(np.max(np.abs(y[48:548])),.1)
        _,_,_,passage_end=c.recover_event(raw,c.SR,metadata,10)
        self.assertEqual(passage_end,7000)
        np.testing.assert_array_equal(raw,original)
        with self.assertRaises(ValueError):
            c.recover_event(raw,c.SR,metadata|{'press_end':16000},1)

    def test_listen_has_both_speeds_jitter_and_no_repeat(self):
        waves={'key':[stroke()*(1+i*.01) for i in range(10)],'space':[stroke()*(1+i*.01) for i in range(3)]}
        y,events=c.phrase(waves,20)
        self.assertEqual(len(y),20*c.SR)
        self.assertEqual({e['wpm'] for e in events},{60,100})
        for part,base in [('key',.55),('space',.6)]:
            ev=[e for e in events if e['part']==part]
            self.assertTrue(all(a['variant']!=b['variant'] for a,b in zip(ev,ev[1:])))
            self.assertTrue(all(.97<=e['rate']<=1.03 and .92<=e['gain']/base<=1.08 for e in ev))
        y2,events2=c.phrase(waves,20)
        self.assertEqual(events,events2)
        np.testing.assert_array_equal(y,y2)


if __name__=='__main__':
    unittest.main()
