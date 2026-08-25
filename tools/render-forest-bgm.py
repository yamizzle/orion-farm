#!/usr/bin/env python3
"""Render an original 16-bit woods loop for Moondrop Mountain."""
from __future__ import annotations
import struct
import wave
from pathlib import Path

SR = 22050
BPM = 80
BEAT = 60.0 / BPM
STEP = BEAT / 2  # eighth notes
ROOT = Path(__file__).resolve().parents[1]
OUT_WAV = ROOT / "assets" / "music" / "forest.wav"

# D dorian (D E F G A B C). 32 bars of 8 eighths (~1:36).
# Intro mist, path, grove, clearing, return. Not G major, not the farm hook.
LEAD = [
    # intro: almost silent, two small flute peeks
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 62, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 64, 0, 0, 0, 0, 0,
    # A path
    62, 0, 0, 64, 65, 0, 64, 0,
    67, 0, 0, 0, 65, 0, 62, 0,
    64, 0, 65, 0, 67, 0, 69, 0,
    67, 0, 0, 0, 62, 0, 0, 0,
    69, 0, 0, 67, 65, 0, 64, 0,
    62, 0, 0, 0, 57, 0, 0, 0,
    60, 0, 62, 0, 64, 0, 0, 0,
    62, 0, 0, 0, 0, 0, 0, 0,
    # B grove, a little higher
    69, 0, 0, 67, 69, 0, 72, 0,
    71, 0, 0, 0, 69, 0, 67, 0,
    65, 0, 67, 0, 69, 0, 0, 0,
    67, 0, 0, 0, 62, 0, 0, 0,
    72, 0, 0, 71, 69, 0, 67, 0,
    65, 0, 0, 0, 64, 0, 62, 0,
    60, 0, 0, 57, 62, 0, 0, 0,
    62, 0, 0, 0, 0, 0, 0, 0,
    # C clearing, longer notes
    62, 0, 0, 0, 0, 0, 64, 0,
    65, 0, 0, 0, 0, 0, 0, 0,
    67, 0, 0, 0, 64, 0, 0, 0,
    62, 0, 0, 0, 0, 0, 0, 0,
    57, 0, 0, 0, 60, 0, 0, 0,
    62, 0, 0, 0, 0, 0, 0, 0,
    64, 0, 0, 65, 67, 0, 0, 0,
    62, 0, 0, 0, 0, 0, 0, 0,
    # return: first half of A, land on D
    62, 0, 0, 64, 65, 0, 64, 0,
    67, 0, 0, 0, 65, 0, 62, 0,
    64, 0, 0, 0, 60, 0, 57, 0,
    62, 0, 0, 0, 0, 0, 0, 0,
]
BASS = [
    # intro
    38, 0, 0, 0, 0, 0, 0, 0,
    38, 0, 0, 0, 0, 0, 0, 0,
    36, 0, 0, 0, 0, 0, 0, 0,
    38, 0, 0, 0, 0, 0, 0, 0,
    # A
    38, 0, 0, 0, 0, 0, 45, 0,
    36, 0, 0, 0, 0, 0, 0, 0,
    43, 0, 0, 0, 0, 0, 0, 0,
    38, 0, 0, 0, 0, 0, 0, 0,
    41, 0, 0, 0, 0, 0, 0, 0,
    38, 0, 0, 0, 0, 0, 0, 0,
    36, 0, 0, 0, 0, 0, 0, 0,
    38, 0, 0, 0, 26, 0, 0, 0,
    # B
    45, 0, 0, 0, 0, 0, 0, 0,
    43, 0, 0, 0, 0, 0, 0, 0,
    41, 0, 0, 0, 0, 0, 0, 0,
    38, 0, 0, 0, 0, 0, 0, 0,
    48, 0, 0, 0, 0, 0, 0, 0,
    41, 0, 0, 0, 0, 0, 0, 0,
    36, 0, 0, 0, 0, 0, 45, 0,
    38, 0, 0, 0, 0, 0, 0, 0,
    # C
    38, 0, 0, 0, 0, 0, 0, 0,
    41, 0, 0, 0, 0, 0, 0, 0,
    43, 0, 0, 0, 0, 0, 0, 0,
    38, 0, 0, 0, 0, 0, 0, 0,
    33, 0, 0, 0, 0, 0, 0, 0,
    38, 0, 0, 0, 0, 0, 0, 0,
    36, 0, 0, 0, 43, 0, 0, 0,
    38, 0, 0, 0, 0, 0, 0, 0,
    # return
    38, 0, 0, 0, 0, 0, 0, 0,
    36, 0, 0, 0, 0, 0, 0, 0,
    36, 0, 0, 0, 33, 0, 0, 0,
    38, 0, 0, 0, 0, 0, 0, 0,
]
ARP = [
    # intro, a few leaves
    0, 0, 74, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 77, 0, 0, 0,
    0, 0, 74, 0, 0, 0, 69, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    # A
    74, 0, 0, 77, 0, 0, 81, 0,
    74, 0, 0, 0, 77, 0, 0, 0,
    76, 0, 0, 79, 0, 0, 81, 0,
    74, 0, 0, 0, 0, 0, 0, 0,
    81, 0, 0, 79, 0, 0, 77, 0,
    74, 0, 0, 0, 69, 0, 0, 0,
    72, 0, 0, 74, 0, 0, 76, 0,
    74, 0, 0, 0, 0, 0, 0, 0,
    # B
    81, 0, 0, 79, 0, 0, 84, 0,
    83, 0, 0, 0, 81, 0, 0, 0,
    77, 0, 0, 79, 0, 0, 81, 0,
    79, 0, 0, 0, 74, 0, 0, 0,
    84, 0, 0, 83, 0, 0, 81, 0,
    77, 0, 0, 0, 76, 0, 0, 0,
    72, 0, 0, 69, 0, 0, 74, 0,
    74, 0, 0, 0, 0, 0, 0, 0,
    # C almost silent
    0, 0, 0, 0, 74, 0, 0, 0,
    0, 0, 0, 0, 77, 0, 0, 0,
    0, 0, 0, 0, 79, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 69, 0, 0, 0,
    0, 0, 0, 0, 74, 0, 0, 0,
    0, 0, 0, 0, 76, 0, 0, 0,
    74, 0, 0, 0, 0, 0, 0, 0,
    # return, thinning
    74, 0, 0, 77, 0, 0, 81, 0,
    74, 0, 0, 0, 77, 0, 0, 0,
    76, 0, 0, 0, 72, 0, 69, 0,
    74, 0, 0, 0, 0, 0, 0, 0,
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
    if not (len(BASS) == n_steps == len(ARP)):
        raise SystemExit("sequence length mismatch %s %s %s" % (n_steps, len(BASS), len(ARP)))
    total = int(n_steps * STEP * SR)
    mix = [0.0] * total
    echo = [0.0] * total
    delay = int(0.46 * SR)

    def place(seq, kind, vol, duty=0.25, max_hold=8):
        for si, note in enumerate(seq):
            if not note:
                continue
            start = int(si * STEP * SR)
            hold = 1
            while si + hold < n_steps and seq[si + hold] == 0:
                hold += 1
                if hold >= max_hold:
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
                    echo[start + i + delay] += s * 0.24

    # Narrower flute-ish lead, quieter leaf arp, roomier bass.
    place(LEAD, "pulse", 0.18, 0.12, 8)
    place(ARP, "pulse", 0.034, 0.08, 4)
    place(BASS, "tri", 0.16, 0.5, 8)
    for i in range(total):
        mix[i] += echo[i]

    lp = [0.0]
    out = []
    peak = 1e-6
    for s in mix:
        y = lowpass(s, lp, 0.16)
        out.append(y)
        peak = max(peak, abs(y))
    gain = 0.70 / peak
    fade = 512
    samples = []
    for i, y in enumerate(out):
        v = y * gain
        if i < fade:
            t = i / float(fade)
            v = v * t + out[total - fade + i] * gain * (1.0 - t)
        elif i >= total - fade:
            v = 0.0
        samples.append(v)

    OUT_WAV.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(OUT_WAV), "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(b"".join(struct.pack("<h", max(-32767, min(32767, int(s * 32767)))) for s in samples))
    print("wrote", OUT_WAV, "seconds", round(total / SR, 2), "bars", n_steps // 8)


if __name__ == "__main__":
    render()
