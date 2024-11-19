import pyaudio
import wave
import sounddevice as sd

# list = sd.query_devices()
# for item in list:
#     if item['hostapi'] == 0:
#         print(item)


# Set up audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, input_device_index=5)

# Record audio for 5 seconds
frames = []
for i in range(0, int(44100 / 10 * 20)):
    data = stream.read(10)
    frames.append(data)

# Stop and close the stream
stream.stop_stream()
stream.close()
p.terminate()

# Save audio to a WAV file
wf = wave.open('output.wav', 'wb')
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)
wf.writeframes(b''.join(frames))
wf.close()