import tkinter as tk
from tkinter import ttk, END
import ctypes
from pytube import YouTube
import os

def clearEntry(input):
   input.delete(0, END)

def downloadMp4(url: str, outpath: str = "./"):
    yt = YouTube(url)
    yt.streams.filter(file_extension="mp4").get_by_resolution("720p").download(outpath)

def downloadMp3(url: str, outpath: str = "./"):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=outpath)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

def checkOption(optionSelected, options, input):
    if optionSelected.get() == options[0]:
        downloadMp4(url=input.get())
        clearEntry(input)
    
    elif optionSelected.get() == options[1]:
        downloadMp3(url=input.get())
        clearEntry(input)

if __name__ == '__main__':

    ctypes.windll.shcore.SetProcessDpiAwareness(True)

    options = ('Download .mp4', 'Download .mp3')

    root = tk.Tk()
    root.title('Mp4/Mp3 downloader')
    root.config(width=600, height=300)
    root.resizable(0, 0)
    root.configure(bg='#2c3840')

    selectOption = ttk.Combobox(root,value=options)
    selectOption.set('Select an option')
    selectOption.place(x = 50, y = 50, width=210, height=35)

    label = ttk.Label(text = "Enter the url of the youtube video you want to download in mp4/mp3").place(x = 50,y = 140)

    entry = ttk.Entry()
    entry.place(x=50, y=100, width=400,height=35)

    button = ttk.Button(text="Download", command=lambda: checkOption(selectOption, options, entry))
    button.place(x=50, y=200)

    root.mainloop()