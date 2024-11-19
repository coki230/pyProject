import sounddevice as sd
import soundfile as sf

# Set parameters for the audio recording
FORMAT = 'INT16'
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# Get the supported audio formats for the audio device
supported_formats = sd.query_hostapis()[0]['supported_formats']

# Check if the desired format is supported
if FORMAT not in supported_formats:
    print("The desired audio format is not supported by the audio device.")
    exit()

# Get the index of the desired audio input device
device_id = 5  # Replace with the correct device ID

# Open a stream for recording
with sd.RawInputStream(samplerate=RATE, channels=CHANNELS, dtype=FORMAT, device=device_id) as stream:
    data = sd.rec(int(RATE * RECORD_SECONDS), samplerate=RATE, channels=CHANNELS, dtype=FORMAT)

# Save the recorded audio to a WAV file
sf.write(WAVE_OUTPUT_FILENAME, data, RATE, subtype='PCM_16')

print("Audio saved to", WAVE_OUTPUT_FILENAME)