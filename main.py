import speech_recognition as sr
import subprocess
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

FOLDER_AUDIO = "audios"
FOLDER_TEXT = "texts"
LANGUAGE = "pt_BR"

print "starting..."

if not os.path.isdir(FOLDER_AUDIO):
    os.mkdir(FOLDER_AUDIO)
    
if not os.path.isdir(FOLDER_TEXT):
    os.mkdir(FOLDER_TEXT)

paths = [os.path.join(FOLDER_AUDIO, nome) for nome in os.listdir(FOLDER_AUDIO)]
files = [arq for arq in paths if os.path.isfile(arq)]
wav_files = [arq for arq in files if arq.lower().endswith(".wav")]

for filename in wav_files:
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)

    command = r.recognize_google(audio, language=LANGUAGE)

    print "running file {}".format(filename)

    filefinal = filename.split("audios\\")[1].split(".wav")[0]
    filefinal = '{}\{}.txt'.format(FOLDER_TEXT, filefinal)
    with open(filefinal, 'w') as arq:
        arq.write(unicode(command))

    print "create a new file {}".format(filefinal)

print "finish"