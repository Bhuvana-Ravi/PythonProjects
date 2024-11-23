import tkinter as tk
from tkinter import *
import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

def speaknow():
    engine.say(textv.get())  # Convert the entered text to speech
    engine.runAndWait()
    engine.stop()

# Create the main window
root = Tk()

# Create a StringVar for text input
textv = StringVar()

# Create a label frame to hold the widgets
obj = LabelFrame(root, text="Text to Speech", font=20, bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

# Create a label for the input text
lbl = Label(obj, text="Enter text", font=30)
lbl.pack(side=tk.LEFT, padx=5)

# Create an entry widget to accept user input
text = Entry(obj, textvariable=textv, font=30, width=25, bd=5)
text.pack(side=tk.LEFT, padx=10)

# Create a button to trigger the speaknow function
btn = Button(obj, text="Speak", font=20, bg="black", fg="white", command=speaknow)
btn.pack(side=tk.LEFT, padx=10)

# Set the window title and size
root.title("Text to Speech")
root.geometry("450x250")
root.resizable(False, False)

# Start the Tkinter event loop
root.mainloop()

              
