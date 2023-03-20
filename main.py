import tkinter as tk
from tkinter import filedialog
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
    outputFolder.config(text=folder)

def download():
    print(folder)
    # get the link from the entry
    link = linkEntry.get()
    # get the format from the option menu
    fileFormat = value_inside.get()
    
    # run the command
    os.system(f"yt-dlp '{link}' -o '{folder}/%(title)s.%(ext)s' -f {fileFormat}")
    print("Link: " + link)
    print("Folder: " + folder)
    print("Title: " + title)


# Create the main window
root = tk.Tk()
# setup window
root.title("YT-DLP")
root.geometry("500x500")


value_inside = tk.StringVar(root)
value_inside.set("Select a format")


# Create a frame
frame = tk.Frame(root)
frame.pack()

# youtube link entry
linkEntry = tk.Entry(frame)
linkEntry.pack()

# output folder picker
outputFolder = tk.Button(frame, text="Output Folder")
outputFolder.config(command=getFolder)
outputFolder.pack()

# format picker
formatPicker = tk.OptionMenu(root, value_inside, *formats)
formatPicker.pack()

tk.StringVar(root)

# Download button
downloadButton = tk.Button(frame, text="Download")
downloadButton.config(command=download)
downloadButton.pack()





root.mainloop()