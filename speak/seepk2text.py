
# # demo 1 using whisper to get the text from the audio file
# import whisper
# model = whisper.load_model("base")
# result = model.transcribe("tts_output.wav")
# print(result["text"])
# ---------------------------------------------------------------------------------------------------

# demo 2 using whisper to get the text from the microphone
import sounddevice as sd
import whisper

def record_audio(duration=5, fs=16000):
    """ Record audio from the microphone. """
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()  # Wait until recording is finished
    return recording.flatten()

def transcribe_and_translate(audio_data, model):
    """ Transcribe and translate the audio using Whisper. """
    result = model.transcribe(audio_data)
    print("Transcription:", result['text'])
    print("Translation (if available):", result.get('translation'))

def main():
    # Load the Whisper model
    model = whisper.load_model("base")

    # Record audio from microphone
    audio_data = record_audio(duration=5)  # Record 5 seconds of audio

    # Process the audio
    transcribe_and_translate(audio_data, model)

if __name__ == "__main__":
    main()


# import sounddevice as sd
# import whisper
# import numpy as np
# import webrtcvad
# import collections
#
# def record_audio_with_vad(fs=16000, frame_duration_ms=30, silence_duration=1):
#     """Record audio from the microphone until silence is detected."""
#     vad = webrtcvad.Vad(1)  # Set aggressiveness from 0 to 3
#     frame_duration = int(fs * frame_duration_ms / 1000)  # frame size in samples
#     num_padding_frames = int(silence_duration * 1000 / frame_duration_ms)
#     ring_buffer = collections.deque(maxlen=num_padding_frames)
#     triggered = False
#     recorded_frames = []
#
#     def callback(indata, frames, time, status):
#         print("callback")
#         nonlocal triggered
#         # Convert to 16-bit PCM format
#         if indata.shape[0] != frame_duration:
#             return  # Skip incorrect frame sizes
#         pcm_data = indata.astype(np.int16).tobytes()
#         is_speech = vad.is_speech(pcm_data, sample_rate=fs)
#
#         if not triggered:
#             print("not triggered")
#             ring_buffer.append((indata.copy(), is_speech))
#             num_voiced = len([f for f, speech in ring_buffer if speech])
#             if num_voiced > 0.9 * ring_buffer.maxlen:
#                 triggered = True
#                 for f, s in ring_buffer:
#                     recorded_frames.append(f)
#                 ring_buffer.clear()
#         else:
#             print("triggered")
#             recorded_frames.append(indata.copy())
#             ring_buffer.append((indata.copy(), is_speech))
#             num_unvoiced = len([f for f, speech in ring_buffer if not speech])
#             if num_unvoiced > 0.9 * ring_buffer.maxlen:
#                 raise sd.CallbackStop
#         print("is_speech", is_speech)
#
#     with sd.InputStream(callback=callback, samplerate=fs, channels=1, dtype='int16', blocksize=frame_duration):
#         sd.sleep(5000)  # Sleep for a long time (will be stopped by callback)
#
#     recording = np.concatenate(recorded_frames, axis=0)
#     return recording.astype(np.float32)
#
# def transcribe_and_translate(audio_data, model):
#     """Transcribe and translate the audio using Whisper."""
#     result = model.transcribe(audio_data)
#     print("Transcription:", result['text'])
#     print("Translation (if available):", result.get('translation'))
#
# def main():
#     # Load the Whisper model
#     model = whisper.load_model("base")
#
#     # Record audio from microphone until silence
#     audio_data = record_audio_with_vad()
#
#     # Process the audio
#     transcribe_and_translate(audio_data, model)
#
# if __name__ == "__main__":
#     main()