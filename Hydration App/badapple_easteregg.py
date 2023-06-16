from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk
from pytube import YouTube
import vlc

import win32gui
import win32con
video_url = "https://www.youtube.com/watch?v=UkgK8eUdpAo"

youtube = YouTube(video_url)
#video = youtube.streams.get_highest_resolution()
#video.download()

root = Tk()
root.title("Project Hydrate: Bad Apple (Easter Egg)")
root.geometry("640x480")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")
    
center_window(root)

folder_path = "G:\My Drive\Hydration App"
root.iconbitmap(default=r"" + folder_path + "\Assets\icon.ico")

video_file_path = folder_path + "\Assets\[HD] Touhou - Bad Apple!! [ＰＶ] (Shadow Art).mp4"

canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()
media = vlc_instance.media_new(video_file_path)
player.set_media(media)
player.set_hwnd(canvas.winfo_id())
player.play()

def stop_video():
    player.stop()
    root.destroy()

stop_button = ttk.Button(root, text="Stop", command=stop_video)
stop_button.pack()

root.mainloop()