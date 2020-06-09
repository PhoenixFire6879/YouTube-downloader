from __future__ import unicode_literals
import youtube_dl
import tkinter as tk
from tkinter import *

def retrieve_input():
    link = entry.get("1.0","end-1c")
    options = {'format': 'best','noplaylist': True,'extract-audio': True,}

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([link])

class PrintLogger():
    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox.configure(state='normal')
        text = text + '\n'
        self.textbox.insert(tk.END, text)
        self.textbox.see(tk.END)
        self.textbox.configure(state='disabled')

    def flush(self):
        pass

root=Tk()
root.title("Vidloader")
root.resizable(width = FALSE, height = FALSE)
root.iconbitmap('./icon.ico')

canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

background_image = tk.PhotoImage(file='bgr.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#e8483c', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.80, relheight=0.1, anchor='n')

entry = tk.Text(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Download", font=40, command=lambda: retrieve_input())
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#e8483c', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.80, relheight=0.6, anchor='n')

t = Text(lower_frame)
t.place(relwidth=1, relheight=1)

pl = PrintLogger(t)
sys.stdout = pl

mainloop()