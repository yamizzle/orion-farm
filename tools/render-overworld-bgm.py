#!/usr/bin/env python3
"""Render an original 16-bit overworld loop for Moondrop Mountain."""
from __future__ import annotations
import math
import struct
import wave
from pathlib import Path

SR = 22050
BPM = 92
BEAT = 60.0 / BPM
STEP = BEAT / 2  # eighth notes
ROOT = Path(__file__).resolve().parents[1]
OUT_WAV = ROOT / "assets" / "music" / "overworld.wav"

# G major. 8 bars of 8 eighths. 0 = rest.
LEAD = [
    67, 0, 71, 0, 74, 0, 71, 0,
    69, 0, 74, 0, 71, 0, 67, 0,
    76, 74, 71, 69, 67, 0, 74, 0,
    71, 69, 67, 0, 62, 0, 0, 0,
    67, 69, 71, 74, 76, 0, 74, 0,
    71, 0, 69, 67, 74, 0, 71, 0,
    69, 0, 67, 64, 62, 0, 67, 0,
    71, 69, 67, 62, 67, 0, 0, 0,
]
BASS = [
    43, 0, 0, 0, 50, 0, 0, 0,
    43, 0, 0, 0, 50, 0, 0, 0,
    48, 0, 0, 0, 43, 0, 0, 0,
    38, 0, 0, 0, 43, 0, 0, 0,
    43, 0, 0, 0, 47, 0, 0, 0,
    50, 0, 0, 0, 47, 0, 0, 0,
    48, 0, 0, 0, 38, 0, 0, 0,
    43, 0, 0, 0, 31, 0, 0, 0,
]
ARP = [
    79, 0, 83, 0, 86, 0, 83, 0,
    79, 0, 83, 0, 86, 0, 83, 0,
    81, 0, 83, 0, 86, 0, 83, 0,
    79, 0, 74, 0, 79, 0, 0, 0,
    79, 0, 83, 0, 86, 0, 83, 0,
    79, 0, 83, 0, 86, 0, 83, 0,
    81, 0, 79, 0, 74, 0, 79, 0,
    83, 0, 79, 0, 74, 0, 67, 0,
]


def midi_hz(n: int) -> float:
    return 440.0 * (2.0 ** ((n - 69) / 12.0))


def pulse(t: float, freq: float, duty: float) -> float:
    if freq <= 0:
        return 0.0
    return 1.0 if (t * freq) % 1.0 < duty else -1.0


def triangle(t: float, freq: float) -> float:
    if freq <= 0:
        return 0.0
    x = (t * freq) % 1.0
    return 4.0 * x - 1.0 if x < 0.5 else 3.0 - 4.0 * x


def env(i: int, n: int, a: int = 40, r: int = 220) -> float:
    if i < a:
        return i / float(a)
    if i > n - r:
        return max(0.0, (n - i) / float(r))
    return 1.0


def lowpass(x, state, alpha=0.18):
    state[0] += alpha * (x - state[0])
    return state[0]


def render():
    n_steps = len(LEAD)
    total = int(n_steps * STEP * SR)
    mix = [0.0] * total
    echo = [0.0] * total
    delay = int(0.38 * SR)

    def place(seq, kind, vol, duty=0.25):
        for si, note in enumerate(seq):
            if not note:
                continue
            start = int(si * STEP * SR)
            # hold into following rests
            hold = 1
            while si + hold < n_steps and seq[si + hold] == 0:
                hold += 1
                if hold >= 4:
                    break
            length = int(hold * STEP * SR * 0.92)
            freq = midi_hz(note)
            for i in range(length):
                if start + i >= total:
                    break
                t = i / float(SR)
                if kind == "pulse":
                    s = pulse(t, freq, duty)
                else:
                    s = triangle(t, freq)
                s *= env(i, length) * vol
                mix[start + i] += s
                if kind == "pulse" and start + i + delay < total:
                    echo[start + i + delay] += s * 0.28

    place(LEAD, "pulse", 0.22, 0.25)
    place(ARP, "pulse", 0.055, 0.125)
    place(BASS, "tri", 0.20, 0.5)
    for i in range(total):
        mix[i] += echo[i]

    lp = [0.0]
    out = []
    peak = 1e-6
    for i, s in enumerate(mix):
        y = lowpass(s, lp, 0.22)
        # tiny one-pole highpass to remove DC
        out.append(y)
        peak = max(peak, abs(y))
    gain = 0.72 / peak
    # seamless loop: crossfade last 512 into first 512
    fade = 512
    samples = []
    for i, y in enumerate(out):
        v = y * gain
        if i < fade:
            t = i / float(fade)
            v = v * t + out[total - fade + i] * gain * (1.0 - t)
        elif i >= total - fade:
            v = 0.0  # already mixed into the start
        samples.append(v)

    OUT_WAV.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(OUT_WAV), "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(b"".join(struct.pack("<h", max(-32767, min(32767, int(s * 32767)))) for s in samples))
    print("wrote", OUT_WAV, "seconds", round(total / SR, 2))


if __name__ == "__main__":
    render()
