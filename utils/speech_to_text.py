import speech_recognition as sr
from pydub import AudioSegment
import ffmpeg

# convert mp3 file to wav  
src=(r"voice_01.mp3")
print(src)
sound = AudioSegment.from_mp3(src)


def convert_ogg_to_wav():
    song = AudioSegment.from_ogg(orig_song)
    song.export(dest_song, format="wav")
    
sound.export("C:/projects/AirtelIQ/outbound_test/voice_01.wav", format="wav")

file_audio = sr.AudioFile(r"C:/projects/AirtelIQ/outbound_test/voice_01.wav")

# use the audio file as the audio source                                        
r = sr.Recognizer()
with file_audio as source:
    audio_text = r.record(source)
print(type(audio_text))
print(r.recognize_google(audio_text))



# #import library
# import speech_recognition as sr
# #Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
# r = sr.Recognizer()
# # Reading Audio file as source
# #  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble
# with sr.AudioFile('voice_02.wav') as source:
#     audio_text = r.listen(source)
# # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
#     try:
#         # using google speech recognition
#         text = r.recognize_google(audio_text)
#         print('Converting audio transcripts into text ...')
#         print(text)
#     except:
#          print('Sorry.. run again...')