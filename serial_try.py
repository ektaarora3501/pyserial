import serial
import time
import speech_recognition as sr

ser = serial.Serial('/dev/ttyACM0', 9600)

m=None

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)

try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

m=r.recognize_google(audio)

while True:
        if(m=='on'):
            val='1'
            ser.write(val.encode("utf-8"))
            break

        elif(m=='close'):
            val='0'
            print(val.encode("utf-8"))
            ser.write(val.encode("utf-8"))

        break
