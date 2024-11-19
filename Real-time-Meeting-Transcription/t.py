import speech_recognition as sr



# get the voice in headphone

def recognize_speech_from_microphone():
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        # Adjust for ambient noise to minimize transcription errors
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Calibration complete. Please speak into the microphone.")

        # Capture the audio
        audio = recognizer.listen(source)

        try:
            # Recognize the speech using Google's Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"Recognized text: {text}")
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    recognize_speech_from_microphone()