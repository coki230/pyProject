# demo 2 using whisper to get the text from the microphone
import sounddevice as sd
import whisper

model = whisper.load_model("base")


def record_audio(duration=5, fs=16000):
    """ Record audio from the microphone. """
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()  # Wait until recording is finished
    return recording.flatten()


def get_voice_text():
    # Record audio from microphone
    audio_data = record_audio(duration=2)  # Record 5 seconds of audio
    print(audio_data.shape)
    print(audio_data)
    result = model.transcribe(audio_data)
    print("Transcription:", result['text'])
    print("Translation (if available):", result.get('translation'))
    return result['text']


def get_text(audio_data):
    print(audio_data.shape)
    print(audio_data)
    result = model.transcribe(audio_data)
    return result['text']


# get_voice_text()