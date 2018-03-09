import math
import numpy
import pyaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=2, rate=44100, output=1)
factor_l = 70 * (math.pi * 2) / 44100 # Frequency Left
factor_r = 90 * (math.pi * 2) / 44100 # Frequency Right
chunk_l = numpy.sin(numpy.arange(44100) * factor_l)
chunk_r = numpy.sin(numpy.arange(44100) * factor_r)
chunk = []
for i in range(len(chunk_l)):
    chunk.append(chunk_l[i] * 0.5) # Volume Left
    chunk.append(chunk_r[i] * 0.5) # Volume Right
chunk = numpy.array(chunk).astype(numpy.float32).tostring()
while True:
    stream.write(chunk)
