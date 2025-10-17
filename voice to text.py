import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the default microphone as the source
with sr.Microphone() as source:
    print("🎤 Say something... (Speak clearly)")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
    audio = recognizer.listen(source)

    print("⌛ Recognizing...")

    try:
        # Use Google Web Speech API to convert speech to text
        text = recognizer.recognize_google(audio)
        print("🗣️ You said:", text)

    except sr.UnknownValueError:
        print("❌ Sorry, I couldn't understand your speech.")
    except sr.RequestError:
        print("⚠️ Could not request results. Check your internet connection.")
