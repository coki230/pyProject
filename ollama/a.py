import ollama
import pyttsx3
engine = pyttsx3.init()

def is_end_sentence(str):
    return str == "," or str == "." or str == "!"


resource = ollama.chat(model="llama3", messages=[
    {
        "role": "user",
        "content": "give me a java demo to login code",
    }
], stream=True)

sentence = ""
for chuck in resource:
    str = chuck["message"]["content"]
    sentence = sentence + str
    print(str, end="", flush=True)
    if is_end_sentence(str):
        engine.say(sentence)
        engine.runAndWait()
        sentence = ""


