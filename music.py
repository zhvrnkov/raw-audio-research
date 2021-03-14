from math import *

fps = 8000
bpm = 240
size = 1/4

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
 
def generate(duration_in_frames: int, step: float, func) -> list:
  output = [0] * duration_in_frames
  value = 0
  for index in range(0, duration_in_frames):
    sample_values = func(value)
    output[index] = func(value)
    value += step
  return output

def sin_wave(duration_in_frames: int, step: float) -> list:
  return generate(duration_in_frames, step, lambda x: int((0.5 + (sin(x) * 0.5)) * max_volume))

def weow_weow(duration_in_frames: int, step: float = 0.01) -> list:
  return generate(
    duration_in_frames, 
    pi / 12, 
    lambda x: 
      (int(x) % 2) * int((0.5 + (sin(x * step) * 0.5)) * max_volume)
  )
 
def write(name: str, notes: list):
  content = bytearray(notes)
  file = open(name, "wb")
  file.write(content)

c = note(261)
d = note(293)
e = note(329)
f = note(349)
g = note(392)
a = note(440)
b = note(493)
n = note(4186)

def track() -> list:
  notes = [
    g, e, d, c,
    d, c, a, g,
    n, g, e, n,
    g, e, d, c,
    c, b, c, c,
    n, c, d, n,
    g, e, d, c,
    d, c, a, g,
    n, g, e, n,
    g, a, d, c,
    b, a, b, c
  ]
  return [freq for note in notes for freq in note]

