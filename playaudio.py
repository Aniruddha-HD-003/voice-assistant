from gtts import gTTS
#from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

def convert_speech(text):
    tts = gTTS(text)
    tts.save("output_audio.mp3")
    
def play_speech():
    audio = AudioSegment.from_mp3("output_audio.mp3")
    audio.export("output.wav", format = "wav")
    play(audio)
    
convert_speech("Hello,What are you doing?")

play_speech()
