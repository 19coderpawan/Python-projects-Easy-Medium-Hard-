# This is a youtube video downloader program using which we can easily download any youtube video by just
# passing it url and also you can save it your local directory.

# first step you have to do is install libraries like yt_dlp , Tkinter .
# to install the yt_dlp use command -: python -m pip install -U yt-dlp

import yt_dlp
import tkinter as tk
from tkinter import filedialog

def Youtube_download(url,save_path):
    try:
        ydl_opts = {
            'format': 'best',  # Download the best quality available
            'outtmpl': '%(title)s.%(ext)s',  # Custom output filename
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Downloaded Successfully")
    except Exception as e:
        print(e)


def open_file_dialog():
    folder=filedialog.askdirectory()
    if folder:
        print(f"Selected folder={folder}")
    return folder

if __name__ == "__main__":
    root=tk.Tk()  #created window object.
    root.withdraw()#so that the window does not appear .

    url=input("enter Youtube video url-:")
    root.deiconify()  # to make the window appear again.
    save_path= open_file_dialog()

    if not save_path:
        print("invalid directory loacation?")
    else:
        Youtube_download(url,save_path)
