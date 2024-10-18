

# This is a YouTube video downloader program using which we can easily download any YouTube video by just
# passing it URL and also you can save it in your local directory.

# the first step you have to do is install libraries like yt_dlp , Tkinter .
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

root=tk.Tk()  #created window object.
root.withdraw()#so that the window does not appear .
