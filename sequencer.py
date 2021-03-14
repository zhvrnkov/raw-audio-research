#!/usr/bin/env python

import os

fps = 8000
bpm = 120
size = 4/4

def note_duration() -> float:
  bps = bpm / 60
  number_of_beats = 4 * size
  return number_of_beats / bps

note_duration_in_frames = int(note_duration() * float(fps))

max_volume = 0xff
min_volume = 0x80

def note(freq: float) -> list:
  output = [0] * note_duration_in_frames
  step = int(fps / freq)
  for frame in range(0, note_duration_in_frames):
    if frame % step:
      output[frame] = max_volume
    else:
      output[frame] = min_volume
  
  return output

def write(name: str, notes: list):
  content = bytearray(notes)
  file = open(name, "wb")
  file.write(content)

def combine_beats(beats: list) -> list:
    beat_len = len(beats[0])
    output = [0] * beat_len
    for index in range(0, beat_len):
        samples_at_index = [beat[index] for beat in beats]
        output[index] = combine_samples(samples_at_index)
    return output

def combine_samples(samples: list) -> int:
    samples_with_volume = list(filter(lambda sample: samples != min_volume, samples))
    output = sum(samples_with_volume) / len(samples_with_volume)
    return int(min(output, max_volume))

def play(samples: list):
    filename = "output.raw"
    open(filename, "wb").write(bytearray(samples))
    os.system(f'./play {filename}')

def flat(xss: list) -> list:
   return [x for xs in xss for x in xs] 

def play_chords(chord_names: list):
    samples = [chords[chord] for chord in chord_names]
    play(flat(samples))

def play_notes(notes: list):
    for note_samples in notes:
        play(note_samples)
 
c = note(261)
cs = note(277)
d = note(293)
ds = note(311)
e = note(329)
f = note(349)
fs = note(369)
g = note(392)
gs = note(415)
a = note(440)
ash = note(466)
b = note(493)
n = note(4186)

chords = {
    k: combine_beats(v) for k, v in {
        "c" : [c, e, g],
        "c#": [cs, f, gs],
        "d" : [d, fs, a],
        "eb": [ds, g, ash],
        "e" : [e, gs, b],
        "f" : [f, a, c],
        "f#": [fs, ash, cs],
        "g" : [g, b, d],
        "ab": [gs, c, ds],
        "a" : [a, cs, e],
        "bb": [ash, d, f],
        "b" : [b, ds, fs]
    }.items()
}

def track() -> list:
    beats = [
        [g, e, d, c],
        [n],
        [d, c, a, g],
        [n, g, e, n],
        [g, e, d, c],
        [c, b, c, c],
        [n, c, d, n],
        [g, e, d, c],
        [d, c, a, g],
        [n, g, e, n],
        [g, a, d, c],
        [b, a, b, c]
    ]
    return [sample for beat in beats for sample in combine_beats(beat)]
