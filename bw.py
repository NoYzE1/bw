import math
import numpy
import pyaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=2, rate=44100, output=1)
while True:
    factor_l = 75 * (math.pi * 2) / 44100
    factor_r = 85 * (math.pi * 2) / 44100
    chunk_l = numpy.sin(numpy.arange(44100) * factor_l)
    chunk_r = numpy.sin(numpy.arange(44100) * factor_r)
    chunk = []
    for i in range(len(chunk_l)):
        chunk.append(chunk_l[i])
        chunk.append(chunk_r[i])
    chunk = numpy.array(chunk).astype(numpy.float32).tostring()
    stream.write(chunk)
