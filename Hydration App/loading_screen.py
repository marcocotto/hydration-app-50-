import os
import tkinter

import subprocess
import sys

import time
import threading

import win32gui
import win32con

import customtkinter
from tkinter import *

from tkinter import ttk
from PIL import Image, ImageTk, ImageFont

 # Change based on where your folder named Hydration App is located
folder_path = "G:\My Drive\Hydration App"

root = Tk()
root.geometry("495x595")

root.iconbitmap(default=r"" + folder_path + "\Assets\icon.ico")

recieved_username =""

if (len(sys.argv) > 1):
    recieved_username = sys.argv[1]
else:
    recieved_username = "NIL"

root.resizable(width=False, height=False)
root.title("Project Hydrate")

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
     
menu_icon = Image.open(r"" + folder_path + "\Assets\IconMain.png")
waves_bottom = Image.open(r"" + folder_path + "\Assets\WavesHalf.png")
title_text_icon = Image.open(r"" + folder_path + "\Assets\TitleText.png")
button_image = Image.open(r"" + folder_path + "\Assets\ButtonImage.png")

progress_bar_image_1 = Image.open(r"" + folder_path + "\Assets\LoadingBar1Percentage.png")
progress_bar_image_2 = Image.open(r"" + folder_path + "\Assets\LoadingBar2Percentage.png")

progress_bar_image_3 = Image.open(r"" + folder_path + "\Assets\LoadingBar3Percentage.png")
progress_bar_image_4 = Image.open(r"" + folder_path + "\Assets\LoadingBar4Percentage.png")

progress_bar_image_5 = Image.open(r"" + folder_path + "\Assets\LoadingBar5Percentage.png")
progress_bar_image_6 = Image.open(r"" + folder_path + "\Assets\LoadingBar6Percentage.png")

menu_icon = menu_icon.resize((108, 141))
waves_bottom = waves_bottom.resize((495, 395))
title_text_icon = title_text_icon.resize((182, 70))

progress_bar_image_1 = progress_bar_image_1.resize((270, 20))
progress_bar_image_2 = progress_bar_image_2.resize((270, 20))

progress_bar_image_3 = progress_bar_image_3.resize((270, 20))
progress_bar_image_4 = progress_bar_image_4.resize((270, 20))

progress_bar_image_5 = progress_bar_image_5.resize((270, 20))
progress_bar_image_6 = progress_bar_image_6.resize((270, 20))

menu_icon_tk = ImageTk.PhotoImage(menu_icon)
waves_bottom_tk = ImageTk.PhotoImage(waves_bottom)
title_text_icon_tk = ImageTk.PhotoImage(title_text_icon)

progress_bar_image_1_tk = ImageTk.PhotoImage(progress_bar_image_1)
progress_bar_image_2_tk = ImageTk.PhotoImage(progress_bar_image_2)

progress_bar_image_3_tk = ImageTk.PhotoImage(progress_bar_image_3)
progress_bar_image_4_tk = ImageTk.PhotoImage(progress_bar_image_4)

progress_bar_image_5_tk = ImageTk.PhotoImage(progress_bar_image_5)
progress_bar_image_6_tk = ImageTk.PhotoImage(progress_bar_image_6)

menu_icon_label = Label(root, image=menu_icon_tk)
waves_bottom_label = Label(root, image=waves_bottom_tk)
title_text_label = Label(root, image=title_text_icon_tk)

loading_message = StringVar()
loading_message.set("LOADING ASSETS")
loading_message_label = Label(root, textvariable=loading_message, fg="darkgray", font=("Arial", 14))

progressbar_1_label = Label(root, image=progress_bar_image_1_tk)
progressbar_2_label = Label(root, image=progress_bar_image_2_tk)

progressbar_3_label = Label(root, image=progress_bar_image_3_tk)
progressbar_4_label = Label(root, image=progress_bar_image_4_tk)

progressbar_5_label = Label(root, image=progress_bar_image_5_tk)
progressbar_6_label = Label(root, image=progress_bar_image_6_tk)

def goto_home_page():
    root.destroy()
    subprocess.Popen(["python", "home.py", recieved_username])

def handle_loading_bar():
    root.after(200, lambda: progressbar_1_label.place(x=110, y=380))
    root.after(600, lambda: progressbar_1_label.place_forget())
    root.after(600, lambda: progressbar_2_label.place(x=110, y=380))
    root.after(750, lambda: loading_message.set("CLEANING UP THINGS"))
    root.after(750, lambda: loading_message_label.place(x=140, y=330))
    root.after(900, lambda: progressbar_2_label.place_forget())
    root.after(900, lambda: progressbar_3_label.place(x=110, y=380))
    root.after(1000, lambda: progressbar_3_label.place_forget())
    root.after(1000, lambda: progressbar_4_label.place(x=110, y=380))
    root.after(1100, lambda: loading_message.set("LOADING USER DATA"))
    root.after(1300, lambda: progressbar_4_label.place_forget())
    root.after(1300, lambda: progressbar_5_label.place(x=110, y=380))
    root.after(2000, lambda: loading_message.set("FINISHING UP"))
    root.after(2000, lambda: loading_message_label.place(x=175, y=330))
    root.after(2500, lambda: progressbar_5_label.place_forget())
    root.after(2500, lambda: progressbar_6_label.place(x=110, y=380))
    root.after(2500, lambda: loading_message.set("LOADED!"))
    root.after(2500, lambda: loading_message_label.place(x=195, y=330))
    root.after(3000, goto_home_page)

style = ttk.Style()
style.configure("TButton", foreground="gray")
style.configure("TButton", font=("Arial", 16))

waves_bottom_label.place(x=-2, y=210)
menu_icon_label.place(x=191, y=40)
title_text_label.place(x=153, y=200)
loading_message_label.place(x=155, y=330)
progressbar_1_label.place(x=110, y=380)

loading_bar_thread = threading.Thread(target=handle_loading_bar)
loading_bar_thread.start()

menu_icon_label.lower(title_text_label)
waves_bottom_label.lower(menu_icon_label)

root.mainloop()