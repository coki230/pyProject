from elevenlabs.client import ElevenLabs
from elevenlabs import play

client = ElevenLabs(api_key="sk_d9644d4f50a0903832822a59cf1b2b4f8426d6433f2bf173")

while True:
    in_txt = input("input: ")
    audio = client.generate(text=in_txt, voice="Rachel",  model="eleven_multilingual_v2")
    play(audio)

# print(client.voices.get_all())
