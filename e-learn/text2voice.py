# import torch
# from parler_tts import ParlerTTSForConditionalGeneration
# from transformers import AutoTokenizer
# import sounddevice as sd
#
# device = "cuda:0" if torch.cuda.is_available() else "cpu"
#
# model = ParlerTTSForConditionalGeneration.from_pretrained("parler-tts/parler-tts-mini-v1").to(device)
# tokenizer = AutoTokenizer.from_pretrained("parler-tts/parler-tts-mini-v1")
# description = "Jon's voice is English teacher, the voice is clearly and smoothly in delivery, and every word must clearly to be understood, with a very close recording that almost has no background noise."
#
#
# def text2voice(text):
#     input_ids = tokenizer(description, return_tensors="pt").input_ids.to(device)
#     prompt_input_ids = tokenizer(text, return_tensors="pt").input_ids.to(device)
#     generation = model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
#     audio_arr = generation.cpu().numpy().squeeze()
#     # sf.write("parler_tts_out.wav", audio_arr, model.config.sampling_rate)
#     sd.play(audio_arr, samplerate=model.config.sampling_rate)
#     sd.wait()


from elevenlabs.client import ElevenLabs
from elevenlabs import play

client = ElevenLabs(api_key="sk_d9644d4f50a0903832822a59cf1b2b4f8426d6433f2bf173")


def get_voice(text):
    return client.generate(text=text, voice="Rachel", model="eleven_multilingual_v2")


def text2voice(text):
    audio = client.generate(text=text, voice="Rachel", model="eleven_multilingual_v2")
    play(audio)
