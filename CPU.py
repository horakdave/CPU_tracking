import psutil
import pyttsx3
import tkinter as tk

engine = pyttsx3.init()

threshold = 90

def update_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > threshold:
        message = "zamn"
        engine.say(message)
        engine.runAndWait()
        cpu_label.config(text="CPU usage is: " + str(cpu_percent) + "%", fg="red")
    else:
        cpu_label.config(text="CPU usage is: " + str(cpu_percent) + "%", fg="black")
    cpu_label.after(1000, update_cpu)

def make_always_on_top():
    root.attributes("-topmost", 1)

root = tk.Tk()
root.title("CPU")
root.geometry("300x50")

cpu_label = tk.Label(root, text="CPU usage is: 0%", font=("Arial", 12))
cpu_label.pack()

update_cpu()

# btn
button = tk.Button(root, text="Make Always On Top", command=make_always_on_top)
button.pack()

root.mainloop()