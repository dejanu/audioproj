# NOTE: this example requires PyAudio because it uses the Microphone class
import os
import speech_recognition as sr
from FirstAudioRead import start_recording

#obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone(device_index=2) as source:
    r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
    print("Say something!")
    audio = r.listen(source)

hard_coded_commands = ['meeting', 'record', ]
user_input = r.recognize_sphinx(audio)

if hard_coded_commands[0] in user_input:
    os.system(r'"C:\Program Files (x86)\Microsoft Office\Office14\OUTLOOK.exe" /c ipm.note.myform /m dejanualex@yahoo.com')
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
elif hard_coded_commands[1] in user_input:
    start_recording()
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
else:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))




# # recognize speech using Sphinx
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

def EnumerateMic():
    """show a list of all available audio inputs"""
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
