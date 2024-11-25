import torch
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer
import sounddevice as sd

device = "mps" if torch.backends.mps.is_available() else "cpu"

model = ParlerTTSForConditionalGeneration.from_pretrained("parler-tts/parler-tts-mini-v1").to(device)
tokenizer = AutoTokenizer.from_pretrained("parler-tts/parler-tts-mini-v1")

prompt = "Hey, how are you doing today?"
description = "Jon's voice is English teacher, the voice is clearly and smoothly in delivery, and every word must clearly to be understood, with a very close recording that almost has no background noise."
input_ids = tokenizer(description, return_tensors="pt").input_ids.to(device)
prompt_input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
generation = model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
audio_arr = generation.cpu().numpy().squeeze()
# sf.write("parler_tts_out.wav", audio_arr, model.config.sampling_rate)
sd.play(audio_arr, samplerate=model.config.sampling_rate)
sd.wait()

# inp = input("Press enter the text you want to convert to audio: ")
# description = "Jon's voice is English teacher, the voice is clearly and smoothly in delivery, and every word must clearly to be understood, with a very close recording that almost has no background noise."
# input_ids = tokenizer(description, return_tensors="pt").input_ids.to(device)
# while inp != "/bye":
#     prompt_input_ids = tokenizer(inp, return_tensors="pt").input_ids.to(device)
#     generation = model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
#     audio_arr = generation.cpu().numpy().squeeze()
#     sd.play(audio_arr, samplerate=model.config.sampling_rate)
#     sd.wait()
#     inp = input("Press enter the text you want to convert to audio: ")