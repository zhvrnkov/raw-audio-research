frames_per_second = 8000
bpm = 120

max_volume = 0xff
min_volume = 0x80

bar_size = 4
note_frame_duration = int(frames_per_second / bar_size)

def note(freq: float) -> list:
  output = [0] * note_frame_duration
  step = int(frames_per_second / freq)
  for frame in range(0, note_frame_duration):
    if frame % step:
      output[frame] = max_volume
    else:
      output[frame] = min_volume
  
  return output
 
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

