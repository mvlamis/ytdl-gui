import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import os

folder = ""
title = ""
extension = ""
fileFormat = ""
formats = ["mp4", "mp3"]


def getFolder():
    global folder
    # get the folder
    folder = filedialog.askdirectory()
    # set the folder to the entry
    outputFolder.configure(text=folder)

def download():
    print(folder)
    # get the link from the entry
    link = linkEntry.get()
    # get the format from the option menu
    fileFormat = formatPicker.get()
    
    # run the command
    os.system(f"yt-dlp '{link}' -o '{folder}/%(title)s.%(ext)s' -f {fileFormat}")
    print("Link: " + link)
    print("Folder: " + folder)
    print("Format: " + fileFormat) 


# Create the main window with customtkinter
root = ctk.CTk()
root.title("Youtube Downloader")
root.geometry("500x500")


value_inside = tk.StringVar(root)
value_inside.set("Select a format")


# Create a frame
frame = ctk.CTkFrame(root)
frame.pack()

# youtube link entry
linkEntry = ctk.CTkEntry(frame)
linkEntry.pack()

# output folder picker
outputFolder = ctk.CTkButton(frame, text="Output Folder")
outputFolder.configure(command=getFolder)
outputFolder.pack()

# format picker
formatPicker = ctk.CTkOptionMenu(frame, values=formats)
formatPicker.pack()

tk.StringVar(root)

# Download button
downloadButton = ctk.CTkButton(frame, text="Download", fg_color="green", hover_color="darkgreen")
downloadButton.configure(command=download)
downloadButton.pack()





root.mainloop()