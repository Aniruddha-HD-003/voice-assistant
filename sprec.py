import speech_recognition as sr


def recognize_speech():
    ''' this recognizes speech '''
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=3)  # Listen for up to 3 seconds

    try:
        if audio:
            text = recognizer.recognize_google(audio)  # Use Google Web Speech API for recognition
            print(text)
            return "You said : "+text
        else:
            return "No audio captured."
    except sr.UnknownValueError:
        return "Speech API could not understand audio"
    except sr.RequestError as e:
        return "Could not request results from  Speech API; {0}".format(e)


print(recognize_speech())
