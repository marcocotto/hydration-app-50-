import os
import tkinter
import subprocess

import win32gui
import win32con

import threading
import time

import customtkinter
from tkinter import *

from tkinter import ttk
from PIL import Image, ImageTk, ImageFont

 # Change based on where your folder named Hydration App is located
folder_path = "G:\My Drive\Hydration App"
folder_path_double = "G:\\My Drive\\Hydration App"
user_logins_file = folder_path_double + "\\db\\user_logins.txt"

root = Tk()
root.geometry("495x595")
root.iconbitmap(default=r"" + folder_path + "\Assets\icon.ico")

root.resizable(width=False, height=False)
root.title("Project Hydrate Log-In")

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

def goto_main_window():
    root.destroy()
    subprocess.Popen(["python", "main.py"])
    
def successful_login(username_returned, real_username):
    root.destroy()
    if not (username_returned == "BADAPPLE"):
        subprocess.Popen(["python", "loading_screen.py", real_username])
    else:
        subprocess.Popen(["python", "badapple_easteregg.py"])

menu_icon = Image.open(r"" + folder_path + "\Assets\IconMain.png")
waves_bottom = Image.open(r"" + folder_path + "\Assets\WavesFullCropped.png")
title_text_icon = Image.open(r"" + folder_path + "\Assets\TitleText.png")
button_image = Image.open(r"" + folder_path + "\Assets\ButtonImage.png")
back_button_image = Image.open(r"" + folder_path + "\Assets\BackButton.png")

menu_icon = menu_icon.resize((108, 141))
waves_bottom = waves_bottom.resize((495, 395))
title_text_icon = title_text_icon.resize((182, 70))
button_image = button_image.resize((200, 30), resample=Image.BICUBIC)
back_button_image = back_button_image.resize((30, 30), resample=Image.BICUBIC)

menu_icon_tk = ImageTk.PhotoImage(menu_icon)
waves_bottom_tk = ImageTk.PhotoImage(waves_bottom)
title_text_icon_tk = ImageTk.PhotoImage(title_text_icon)
button_image_tk = ImageTk.PhotoImage(button_image)
back_button_image_tk = ImageTk.PhotoImage(back_button_image)

menu_icon_label = Label(root, image=menu_icon_tk)
waves_bottom_label = Label(root, image=waves_bottom_tk)
title_text_label = Label(root, image=title_text_icon_tk)
back_button = ttk.Button(root, image=back_button_image_tk, compound="center", width=0, command=goto_main_window)

username_variable = StringVar()
username_variable.set("")

verifying_username = StringVar()
verifying_username.set("")

password_variable = StringVar()
password_variable.set("")

username_changed = BooleanVar()
username_changed.set(False)

password_changed = BooleanVar()
password_changed.set(False)

username_warning_showing = BooleanVar()
username_warning_showing.set(False)

password_warning_showing = BooleanVar()
password_warning_showing.set(False)

def usernamenonexistent_warning():
    if not (username_warning_showing.get()):
        username_warning_showing.set(True)
        username_non_existent_label.place(x=170, y=370)
        
        time.sleep(2)
        username_non_existent_label.place_forget()
        username_warning_showing.set(False)

def wrongpassword_warning():
    if not (password_warning_showing.get()):
        password_warning_showing.set(True)
        wrong_password_label.place(x=185, y=410)
        
        time.sleep(2)
        wrong_password_label.place_forget()
        password_warning_showing.set(False)
    
def send_login_request():
    if (username_changed.get() == True and password_changed.get() == True):
        #print("User logged in with user:", username_variable.get(), "and password:", password_variable.get())
        
        verifying_username.set(username_variable.get().strip().upper())        
        user_logins = open(user_logins_file, "r")
        user_logins_lines = user_logins.readlines()
        
        user_exists = BooleanVar()
        user_exists.set(False)
        
        for user_login in user_logins_lines:
            if verifying_username.get().strip() in user_login:
                login_info = user_login.split("=")
                user = login_info[1]
                password = login_info[2]
                
                if (user.strip() == verifying_username.get().strip()):
                    user_exists.set(True)
                    
                    if (password.strip() == password_variable.get().strip()):
                        #print("User " + user.strip() + " successfully logged in!")
                        successful_login(user.strip(), login_info[3].strip())
                    else:
                        print("Incorrect password")
                        if not (password_warning_showing.get()):
                            password_warning_thread = threading.Thread(target=wrongpassword_warning)
                            password_warning_thread.start()
                
        if (user_exists.get() == False):
            if not (username_warning_showing.get()):
                username_warning_thread = threading.Thread(target=usernamenonexistent_warning)
                username_warning_thread.start()
            
            return
    else:
        print("Log-in rejected as one or both the inputs were left blank")

login_button = ttk.Button(root, text="L O G  I N", image=button_image_tk, compound="center", command=send_login_request)
login_label = Label(root, text="A C C O U N T  L O G  I N", fg="darkgray", font=("Arial", 14))

wrong_password_label = ttk.Label(root, text="Incorrect Password", foreground="red", font=("Arial", 10))
username_non_existent_label = ttk.Label(root, text="Username does not exist", foreground="red", font=("Arial", 10))

style = ttk.Style()
style.configure("TButton", foreground="gray")
style.configure("TButton", font=("Arial", 16))

waves_bottom_label.place(x=-2, y=210)
menu_icon_label.place(x=191, y=40)

title_text_label.place(x=153, y=200)
back_button.place(x=20, y=20)

def username_focus(event):
    if (username_box.get() == "Username"):
        if (username_changed.get() == False):
            username_changed.set(True)
            username_box.delete(0, len(username_box.get()))
            username_box.configure(foreground="black")

def username_leave(event):
    if (username_box.get() == ""):
        if (username_changed.get() == True):
            username_changed.set(False)
            username_box.insert(0, "Username")
            username_box.configure(foreground="gray")

def password_focus(event):
    if (password_box.get() == "Password"):
        if (password_changed.get() == False):
            password_changed.set(True)
            password_box.delete(0, len(password_box.get()))
            password_box.configure(foreground="black", show="*")

def password_leave(event):
    if (password_box.get() == ""):
        if (password_changed.get() == True):
            password_changed.set(False)
            password_box.insert(0, "Password")
            password_box.configure(foreground="gray", show="")

username_box = ttk.Entry(root, textvariable=username_variable, width=34, foreground="gray")
password_box = ttk.Entry(root, textvariable=password_variable, width=34, foreground="gray")

username_box.insert(0, "Username")
username_box.bind("<FocusIn>", username_focus)
username_box.bind("<FocusOut>", username_leave)

password_box.insert(0, "Password")
password_box.bind("<FocusIn>", password_focus)
password_box.bind("<FocusOut>", password_leave)

login_label.place(x=130, y=310)
username_box.place(x=140, y=350)

password_box.place(x=140, y=390)
login_button.place(x=140, y=430)

title_text_label.lower(login_button)
menu_icon_label.lower(title_text_label)
waves_bottom_label.lower(menu_icon_label)

root.mainloop()