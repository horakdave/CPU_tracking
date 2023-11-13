# a simple python code that lets you know if you're using too much CPU in text to speech

import psutil
import pyttsx3

engine = pyttsx3.init()

threshold = 99

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > threshold:
        print("CPU usage is:", cpu_percent, "%")
        message = "STOP"
        engine.say(message)
        engine.runAndWait()
    else:
        print("CPU usage is:", cpu_percent, "%")
