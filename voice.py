from TTS.api import TTS
tts = TTS("tts_models/en/multi-dataset/tortoise-v2")

# # cloning `lj` voice from `TTS/tts/utils/assets/tortoise/voices/lj`
# # with custom inference settings overriding defaults.
# tts.tts_to_file(text="Hello, my name is Manmay , how are you?",
#                 file_path="output.wav",
#                 voice_dir="voices/",
#                 speaker="lj",
#                 num_autoregressive_samples=1,
#                 diffusion_iterations=10)
#
# # Using presets with the same voice
# tts.tts_to_file(text="Hello, my name is Manmay , how are you?",
#                 file_path="output.wav",
#                 voice_dir="voices/",
#                 speaker="lj",
#                 preset="ultra_fast")

# Random voice generation
tts.tts_to_file(text="你好",
                file_path="output.wav")