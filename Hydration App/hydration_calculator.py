import os
import tkinter

import subprocess
import sys

import win32gui
import win32con
from tkinter import *

import tkinter as ttk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk, ImageFont

# Change based on where your folder named Hydration App is located
folder_path = "G:\My Drive\Hydration App"

root = Tk()
root.geometry("495x595")

root.iconbitmap(default=r"" + folder_path + "\Assets\icon.ico")
logged_in_username = ""

folder_path_double = "G:\\My Drive\\Hydration App"
user_data_file = folder_path_double + "\\db\\user_data.txt"

if (len(sys.argv) > 1):
    logged_in_username = sys.argv[1]
else:
    logged_in_username = "NIL"
    
root.resizable(width=False, height=False)
root.title("Project Hydrate: Hydration Calculator")

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

def goto_home_window():
    root.destroy()
    subprocess.Popen(["python", "home.py", logged_in_username])

def calculate_hydration():
    weight = int(weight_entry.get())
    gender = gender_var.get()
    activity_level = activity_var.get()

    base_hydration = 0
    hydration_multiplier = 1.0
    base_hydration += weight * 0.03

    if (gender == "Male"):
        base_hydration += 0.2
    elif (gender == "Female"):
        base_hydration -= 0.1

    if (activity_level == "Rarely active"):
        hydration_multiplier += 0.1
    elif (activity_level == "Somewhat active"):
        hydration_multiplier += 0.2
    elif (activity_level == "Quite active"):
        hydration_multiplier += 0.3
    elif (activity_level == "Extremely active"):
        hydration_multiplier += 0.4

    recommended_hydration = int(round(base_hydration * hydration_multiplier, 4) * 1000)
    result_label.config(text="Recommended hydration: {} liters".format(recommended_hydration / 1000))
    
    user_found = BooleanVar()
    user_found.set(False)
        
    user_data = open(user_data_file, "r+")
    lines = user_data.readlines()
        
    for index, line in enumerate(lines):
        if logged_in_username.upper().strip() in line:
            user_found.set(True)
            line_list = line.split("=")
            new_line = "{}={}={}".format(logged_in_username.upper().strip(), str(recommended_hydration).strip(), line_list[2])
            
            lines[index] = new_line
            user_data.seek(0)
            
            user_data.writelines(lines)
            user_data.truncate()
            return
        
    if not (user_found.get() == True): 
        line_list = line.split("=")       
        user_data.write("{}={}={}\n".format(logged_in_username.upper().strip(), str(recommended_hydration).strip(), 0))
        user_data.close()
        return


back_button_image = Image.open(r"" + folder_path + "\Assets\BackButton.png")
back_button_image = back_button_image.resize((30, 30), resample=Image.BICUBIC)

back_button_image_tk = ImageTk.PhotoImage(back_button_image)
back_button = ttk.Button(root, image=back_button_image_tk, compound="center", width=0, command=goto_home_window)
back_button.place(x=20, y=20)

weight_label = ttk.Label(root, text="Weight (in kg):")
weight_label.pack()
weight_entry = ttk.Entry(root)
weight_entry.pack()

gender_label = ttk.Label(root, text="Gender:")
gender_label.pack()
gender_var = StringVar()
gender_var.set("Male")
gender_male_radiobutton = ttk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
gender_male_radiobutton.pack()
gender_female_radiobutton = ttk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
gender_female_radiobutton.pack()

activity_label = ttk.Label(root, text="Activity Level:")
activity_label.pack()
activity_var = StringVar()
activity_var.set("Rarely active")
activity_radiobuttons = [
    "Rarely active",
    "Somewhat active",
    "Quite active",
    "Extremely active"
]

for activity in activity_radiobuttons:
    activity_radiobutton = ttk.Radiobutton(root, text=activity, variable=activity_var, value=activity)
    activity_radiobutton.pack()

calculate_button = ttk.Button(root, text="Calculate", command=calculate_hydration)
calculate_button.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()