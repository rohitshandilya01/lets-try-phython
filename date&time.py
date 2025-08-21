import tkinter as tk
from time import strftime

root = tk.Tk()  # Fixed: should be Tk() not tk()
root.title("Digital Clock")


def time():
    string = strftime('%H:%M:%S')  # Added format for time
    label.config(text=string)      # Fixed: text=string, not text-string
    label.after(1000, time)

label = tk.Label(root, font=('Poppins', 50, 'bold'), background='yellow', foreground='black')  # Fixed: Label not label

label.pack(anchor='center')
time()
root.mainloop()