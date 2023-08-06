import os
from PyPDF2 import PdfReader
import docx2txt
from tkinter import *
from tkinter import filedialog,messagebox
from tkinter.simpledialog import askstring
import pyttsx3


window=Tk()
window.title("pdf to audio")
window.config(padx=250,pady=50)
window.minsize(width=500, height=500,)


def open_file_path():
    file_path = filedialog.askopenfilename(filetypes=(("pdf files", "*.pdf"), ("doc files", "*.doc"), ("docx files", "*.docx"), ("text files", "*.txt")))
    filename_label.config(text=file_path.split("/")[-1].split(".")[0])
    window.update()
    extension=file_path.split("/")[-1].split(".")[1]
    if extension=="pdf":
        pdf_reader(file_path)
    elif extension=="docx":
        doc = docx2txt.process(file_path)
        print(doc)
        audio_conversion(doc,file_path)
    elif extension=="txt":
        with open(file_path) as file:
             audio_conversion(file.read(),file_path)
    else:
        messagebox.showwarning(title="Error",
                               message="Select a valid file.")



def pdf_reader(file_path):
    entire_text_string = ""
    reader = PdfReader(file_path)
    print(len(reader.pages))
    for i in range(0,len(reader.pages)):
        text = reader.pages[i].extract_text().split(".")
        entire_text=".".join(text)
        entire_text_string+=entire_text
    print(entire_text_string)
    audio_conversion(entire_text_string,file_path)
def audio_conversion(text,file_path):
    new_file_name = askstring('Name', 'Enter the audio file name')

    x = file_path.split("/")[:-1]


    new_path = "/".join(x)
    altered_path = new_path + "/"
    folder_path = new_path + "/" + "audio-files/"
    if os.path.exists(folder_path):
        print("yes")
        print(folder_path)
    else:
        print("no")
        os.mkdir(folder_path)

    # try:
    final_filepath = folder_path+new_file_name
    print(final_filepath)
    if os.path.exists(final_filepath):
        messagebox.showwarning(title="Warning",
                               message=f"Error: '{new_file_name}.mp3' already exists!")
        new_file_name = askstring('Name', 'Enter the new name')
        final_filepath = os.path.join(folder_path, f"{new_file_name}")
        engine = pyttsx3.init()
        # engine.say(text)
        engine.save_to_file(text, f'{final_filepath}.mp3')
        engine.runAndWait()

        messagebox.showinfo(title="Success",
                            message="Audio saved in 'audio-files' folder at original location.")

    else:
        engine = pyttsx3.init()
        # engine.say(text)
        engine.save_to_file(text, f'{final_filepath}.mp3')
        engine.runAndWait()

        messagebox.showinfo(title="Success",
                            message="Audio saved in 'audio-files' folder at original location.")





title_label=Label(text="Text to Audio Conversion",padx=10,pady=10)
title_label.grid(row=0,column=0,columnspan=2)
filename_label=Label(window,text="Open File",padx=10,pady=10)
filename_label.grid(row=1,column=0)

open_button=Button(window,text="Open",padx=10,pady=10,command=open_file_path)
open_button.grid(row=1,column=1)

# creating a pdf reader object


# reader = PdfReader('example.pdf')

# printing number of pages in pdf file

# getting a specific page from the pdf file

#

#################################
# # The text that you want to convert to audio
# # mytext = 'Welcome to geeksforgeeks!'
# mytext = text
#
# # Language in which you want to convert
# language = 'en'
#
# # Passing the text and language to the engine,
# # here we have marked slow=False. Which tells
# # the module that the converted audio should
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
#
# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save("welcome.mp3")
#
# # Playing the converted file
# os.system("welcome.mp3")

window.mainloop()