import psutil
import pyttsx3
import tkinter as tk

engine = pyttsx3.init()

threshold = 90

def update_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > threshold:
        message = "your CPU is at 90%"
        engine.say(message)
        engine.runAndWait()
        cpu_label.config(text="CPU usage is: " + str(cpu_percent) + "%", fg="red")
    else:
        cpu_label.config(text="CPU usage is: " + str(cpu_percent) + "%", fg="black")
    cpu_label.after(1000, update_cpu)

root = tk.Tk()
root.title("CPU")
root.geometry("300x50")

cpu_label = tk.Label(root, text="CPU usage is: 0%", font=("Arial", 12))
cpu_label.pack()

update_cpu()

root.mainloop()
