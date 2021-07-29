# pip3 install gTTS pyttsx3 playsound
# https://www.thepythoncode.com/article/convert-text-to-speech-in-python#Online_Text_to_speech
import gtts
# from playsound import playsound
# pip install pydub
from pydub import AudioSegment

def generate_mp3(filename):
    # Use a breakpoint in the code line below to debug your script.
    text = read_file(filename)
    # tts = gtts.gTTS(text, lang="es")
    tts = gtts.gTTS(text, lang="es-us")
    # save the audio file
    tts.save("audio.mp3")

def read_file(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    return text

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_mp3('text.txt')
    # sound = AudioSegment.from_mp3("audio.mp3")
    # fast_sound = speed_change(sound, 1.25)
    # fast_sound.export("audio2.mp3", format="mp3")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
