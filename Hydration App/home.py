import os
import tkinter

import subprocess
import sys

import win32gui
import win32con

import customtkinter
from tkinter import *

import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk, ImageFont, ImageFilter

 # Change based on where your folder named Hydration App is located
folder_path = "G:\My Drive\Hydration App"
folder_path_double = "G:\\My Drive\\Hydration App"

root = Tk()
root.geometry("495x595")

root.iconbitmap(default=r"" + folder_path + "\Assets\icon.ico")
user_data_file = folder_path_double + "\\db\\user_data.txt"

logged_in_username = ""

if (len(sys.argv) > 1):
    logged_in_username = sys.argv[1]
    
def goto_main_window():
    root.destroy()
    subprocess.Popen(["python", "main.py", logged_in_username])
    
def goto_calculator_window():
    root.destroy()
    subprocess.Popen(["python", "hydration_calculator.py", logged_in_username])
    
print(logged_in_username)

root.resizable(width=False, height=False)
root.title("Project Hydrate: Home")

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
waves_bottom = Image.open(r"" + folder_path + "\Assets\WavesFullCropped.png")
title_text_icon = Image.open(r"" + folder_path + "\Assets\TitleText.png")
button_image = Image.open(r"" + folder_path + "\Assets\ButtonImage.png")
user_icon = Image.open(r"" + folder_path + "\Assets\IconUser.png")
waves_top = Image.open(r"" + folder_path + "\Assets\TopWaves.png")

title_text_icon.convert('RGBA')

menu_icon = menu_icon.resize((108, 141))
waves_bottom = waves_bottom.resize((495, 395))
title_text_icon = title_text_icon.resize((182, 70))
button_image = button_image.resize((200, 30), resample=Image.BICUBIC)
user_icon = user_icon.resize((100, 100))
waves_top = waves_top.resize((495, 595))

menu_icon_tk = ImageTk.PhotoImage(menu_icon)
waves_bottom_tk = ImageTk.PhotoImage(waves_bottom)

title_text_icon_tk = ImageTk.PhotoImage(title_text_icon)
button_image_tk = ImageTk.PhotoImage(button_image)

user_icon_tk = ImageTk.PhotoImage(user_icon)
waves_top_tk = ImageTk.PhotoImage(waves_top)

menu_icon_label = Label(root, image=menu_icon_tk)
waves_bottom_label = Label(root, image=waves_bottom_tk)

title_text_label = Label(root, image=title_text_icon_tk)
user_icon_label = Label(root, image=user_icon_tk)
waves_top_label = Label(root, image=waves_top_tk)

username_variable = StringVar()
username_variable.set("")

hydration_progress_variable = StringVar()
hydration_progress_variable.set("")

if not (logged_in_username == ""):
    username_variable.set(str(logged_in_username) + "!")
else:
    logged_in_username = "NIL"
    username_variable.set("NIL!")

user_data = open(user_data_file, "r+")
lines = user_data.readlines()

user_found = BooleanVar()
user_found.set(False)
        
for index, line in enumerate(lines):
    if logged_in_username.upper().strip() in line:
        user_found.set(True)
        line_list = line.split("=")
        hydration_progress_variable.set("HYDRATION PROGRESS: {}ml / {}ml".format(line_list[2].strip().replace(".", ""), line_list[1].strip().replace(".", "")))
        break
    
if (user_found.get() == False):
    hydration_progress_variable.set("Recommended Hydration not yet Calculated")

hydration_progress_label = Label(root, textvariable=hydration_progress_variable, fg="black", font=("Simplifica", 15))
signin_options_label = Label(root, textvariable=username_variable, fg="black", font=("Simplifica", 20, "bold"))
hello_label = Label(root, text="HELLO", fg="black", font=("Simplifica", 20))
signup_button = ttk.Button(root, text="L O G  O U T", image=button_image_tk, compound="center", command=goto_main_window)
calculator_button = ttk.Button(root, text="C A L C U L A T O R", image=button_image_tk, compound="center", command=goto_calculator_window)

style = ttk.Style()
style.configure("TButton", foreground="gray")
style.configure("TButton", font=("Arial", 16))

waves_top_label.place(x=-2, y=-100)
waves_bottom_label.place(x=-2, y=210)
title_text_label.place(x=153, y=80)
hello_label.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
signin_options_label.place(relx=0.5, rely=0.55, anchor = tk.CENTER)
hydration_progress_label.place(relx=0.5, rely=0.6, anchor = tk.CENTER)
user_icon_label.place(relx=0.5, y=220, anchor = tk.CENTER)
signup_button.place(x=140, y=450)
calculator_button.place(x=140, y=400)

waves_top_label.lower(waves_bottom_label)
menu_icon_label.lower(title_text_label)
waves_bottom_label.lower(menu_icon_label)

root.mainloop()