import tkinter
from tkinter import *
from tkinter import filedialog
import os
import youtube_dl

window = tkinter.Tk()
window.geometry('1280x720')
window.title("YOU TUBE VIDEO DOWNLOADER")
folder_path = StringVar()


def clr_button():
    enter1.delete(first=0, last=20)


def fopen():
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)


def download():
    URL = enter1.get()
    PATH = enter2.get()
    ydl_opts = {}
    os.chdir(PATH)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        window.title('Downloading... ' + URL)
        ydl.download([URL])
    print(ydl_opts)
    noti = 'your video downloaded'
    window.title(noti)
    Notification.configure(text=noti, fg='black', bg="SpringGreen3", width=50, font=('times', 17, 'bold', 'italic'))
    Notification.place(x=350, y=500)


label1 = Label(window, text="Enter URL--->", font=('italic', 14, 'bold'), fg='blue')
label1.place(x=100, y=60)

label2 = Label(window, text="Choose Path--->", font=('italic', 14, 'bold'), fg='blue')
label2.place(x=100, y=140)

Notification = Label(window, text='video downloaded from Nishit Patel', bg='green', fg="white", width=35,
                     height=3, font=('times', 17, 'bold'))

label3 = Label(window, text='@Developed By NishitPatel', font=('italic', 28, 'bold'), fg='black', bg='yellow')
label3.place(x=370, y=500)

enter1 = Entry(window, font=('arial', 12, 'bold'), width=28)
enter1.place(x=350, y=65)

enter2 = Entry(window, font=('arial', 12, 'bold'), width=28, textvariable=folder_path)
enter2.place(x=350, y=145)

button1 = Button(window, text="Clear", fg='yellow', bg='green', activebackground='blue', width=14, command=clr_button)
button1.place(x=620, y=64)

button2 = Button(window, text="Browse", fg='yellow', bg='green', activebackground='blue', width=14, command=fopen)
button2.place(x=620, y=143)

button3 = Button(window, text="Download", width=20, font=6, fg='red', bg='black', activebackground='black',
                 command=download)
button3.place(x=400, y=250)
window.mainloop()
