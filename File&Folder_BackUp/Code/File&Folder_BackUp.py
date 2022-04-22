from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import filedialog
import os

from DatabaseOperation import EncryptData
from DatabaseOperation import DecryptData

root = Tk()
root.geometry("650x200")
root.title("Take Back-up for File or Folder")
root.resizable(0,0)

File_Name = ""
Folder_Name = ""

def clearWindow():
    widget_list = root.grid_slaves()
    for widget in widget_list:
        widget.destroy()

def Home_Page():
    global File_Name
    global Folder_Name
    clearWindow()

    # Reset Values for Each Entry
    File_Name = ""
    Folder_Name = ""

    Button(text="Take Back Up", padx=20, bg="cyan", font="Verdana 10 bold", command=lambda: Take_BackUp_Page()).grid(pady=50, padx=80, row=0, column=0)
    Button(text="Extract Back Up", bg="cyan", font="Verdana 10 bold", command=lambda: Extract_BackUp_Page()).grid(pady=50, padx=80, row=0, column=1)

def Take_BackUp_Page():
    clearWindow()

    Button(text="File Back Up", padx=20, bg="cyan", font="Verdana 10 bold", command=lambda: File_BackUp_Page()).grid(pady=50, padx=90, row=0, column=0)
    Button(text="Folder Back Up", bg="cyan", font="Verdana 10 bold", command=lambda: Folder_BackUp_Page()).grid(pady=50, padx=90, row=0, column=1)

def File_BackUp_Page():
    global File_Name
    clearWindow()

    Frame_1 = Frame()
    Frame_1.grid(row=0, column=0)
    Frame_2 = Frame()
    Frame_2.grid(row=1, column=0)
    Frame_3 = Frame()
    Frame_3.grid(row=1, column=0)

    Label(Frame_1, text="File Name", font="Verdana 10 bold").grid(padx=5, pady=5, row=0, column=0)
    Text_Field = Text(Frame_1, height=1, width=40)
    Text_Field.insert(INSERT, "")
    Text_Field.grid(padx=5, pady=5, row=0, column=1)
    Button(Frame_1, text="Browse File", bg="cyan", command=lambda: browse_file(Text_Field)).grid(padx=5, pady=5, row=0, column=2)

    # True represents if it is a File Back Up
    Button(Frame_2, text="Take Back Up", bg="cyan", command=lambda: validate_FileorFolder(File_Name, True, Frame_3)).grid(padx=5, pady=5, row=0, column=0)

def Folder_BackUp_Page():
    global Folder_Name
    clearWindow()

    Frame_1 = Frame()
    Frame_1.grid(row=0, column=0)
    Frame_2 = Frame()
    Frame_2.grid(row=1, column=0)
    Frame_3 = Frame()
    Frame_3.grid(row=2, column=0)

    Label(Frame_1, text="Folder Name", font="Verdana 10 bold").grid(padx=5, pady=5, row=0, column=0)
    Text_Field = Text(Frame_1, height=1, width=40)
    Text_Field.insert(INSERT, "")
    Text_Field.grid(padx=5, pady=5, row=0, column=1)
    Button(Frame_1, text="Browse Folder", bg="cyan", command=lambda: browse_folder(Text_Field)).grid(padx=5, pady=5, row=0, column=2)

    # False represents if it is a File Back Up
    Button(Frame_2, text="Take Back Up", bg="cyan", command=lambda: validate_FileorFolder(Folder_Name, False, Frame_3)).grid(padx=5, pady=5, row=0, column=0)

def browse_file(Text_Field):
    global File_Name

    File_Name = filedialog.askopenfilename(initialdir = "/")
    File_Name = File_Name.replace("/", "\\", File_Name.count('/'))
    Text_Field.delete("1.0", END)
    Text_Field.insert(INSERT, File_Name)

def browse_folder(Text_Field):
    global Folder_Name

    Folder_Name = filedialog.askdirectory(initialdir = "/")
    Folder_Name = Folder_Name.replace("/", "\\", Folder_Name.count('/'))
    Text_Field.delete("1.0", END)
    Text_Field.insert(INSERT, Folder_Name)

def validate_FileorFolder(File_or_Folder_Name, ifFileBackUp, Frame_3):
    if File_or_Folder_Name == "":
        # No File or Folder is Browsed
        tmsg.showinfo("Error", "Please Browse a valid entry")
    else:
        if ifFileBackUp:
            # If File Name is abcd.txt
            # Back Up will be captured in abcd.db
            # abcd.db will be created at same level of File
            _File_or_Folder_Name = File_or_Folder_Name.split(".")
            _File_or_Folder_Name.pop()
            BackUp_FileName = ".".join(_File_or_Folder_Name) + ".db"

            File_List = [File_or_Folder_Name]
        else:
            # If Folder Name is ABCD
            # Back Up will be captured in ABCD.db
            # ABCD.db will be created at same level of Folder
            BackUp_FileName = File_or_Folder_Name + ".db"

            # Recursively Capture all File Name from that Folder
            File_List = []
            for r, d, f in os.walk(File_or_Folder_Name):
                for file in f:
                    File_List.append(os.path.join(r, file))

        _File_or_Folder_Name = File_or_Folder_Name.split("\\")
        _File_or_Folder_Name.pop()
        _File_or_Folder_Name = "\\".join(_File_or_Folder_Name)
        ifBackUpSuccessful = EncryptData.takeBackUp(File_List, BackUp_FileName, ifFileBackUp, _File_or_Folder_Name, Frame_3)

        if ifBackUpSuccessful:
            # Back Up is successfully Complted
            clearWindow()

            Frame_1 = Frame()
            Frame_1.grid(row=0, column=0)
            Frame_2 = Frame()
            Frame_2.grid(row=1, column=0)
            Frame_3 = Frame()
            Frame_3.grid(row=2, column=0)

            Label(Frame_1, text="Back Up is Successful", fg="green", font="Verdana 20 bold").grid(padx=5, pady=10, row=0, column=0)
            Label(Frame_2, text="Back Up File", font="Verdana 10 bold").grid(padx=5, pady=10, row=0, column=0)
            Text_Field = Text(Frame_2, height=1, width=40)
            Text_Field.insert(INSERT, BackUp_FileName)
            Text_Field.grid(padx=5, pady=10, row=0, column=1)
            Button(Frame_3, text="Return To Main Page", bg="cyan", command=lambda: Home_Page()).grid(pady=10)
        else:
            # Back Up is Failed due to some reason
            clearWindow()

            Frame_1 = Frame()
            Frame_1.grid(row=0, column=0)
            Frame_2 = Frame()
            Frame_2.grid(row=1, column=0)

            Label(Frame_1, text="Back Up is Failed", fg="red", font="Verdana 20 bold").grid(pady=10)
            Button(Frame_2, text="Return To Main Page", bg="cyan", command=lambda: Home_Page()).grid(pady=10)

def Extract_BackUp_Page():
    global Folder_Name
    global File_Name
    clearWindow()

    Frame_1 = Frame()
    Frame_1.grid(row=0, column=0)
    Frame_2 = Frame()
    Frame_2.grid(row=1, column=0)
    Frame_3 = Frame()
    Frame_3.grid(row=2, column=0)

    Label(Frame_1, text="Back Up File Name", font="Verdana 10 bold").grid(padx=5, pady=5, row=0, column=0)
    BackUpFile_Text_Field = Text(Frame_1, height=1, width=40)
    BackUpFile_Text_Field.insert(INSERT, "")
    BackUpFile_Text_Field.grid(padx=5, pady=5, row=0, column=1)
    Button(Frame_1, text="Browse File", bg="cyan", padx=10, command=lambda: browse_file(BackUpFile_Text_Field)).grid(padx=5, pady=5, row=0, column=2)

    Label(Frame_1, text="Destination Folder Name", font="Verdana 10 bold").grid(padx=5, pady=5, row=1, column=0)
    DestinationFolder_Text_Field = Text(Frame_1, height=1, width=40)
    DestinationFolder_Text_Field.insert(INSERT, "")
    DestinationFolder_Text_Field.grid(padx=5, pady=5, row=1, column=1)
    Button(Frame_1, text="Browse Folder", bg="cyan", command=lambda: browse_folder(DestinationFolder_Text_Field)).grid(padx=5, pady=5, row=1, column=2)

    # False represents if it is a File Back Up
    Button(Frame_2, text="Extract Back Up", bg="cyan", command=lambda: validate_Folder(Folder_Name, File_Name, Frame_3)).grid(padx=5, pady=5, row=0, column=0)

def validate_Folder(Destination_Folder_Name, BackUp_File_Name, Frame_3):
    if BackUp_File_Name == "":
        # No Back Up file selected
        tmsg.showinfo("Error", "Please Browse Back Up File")
    else:
        if not BackUp_File_Name.endswith(".db"):
            # No .db file selected
            tmsg.showinfo("Error", "Please Browse valid Back Up file")
        else:
            if Destination_Folder_Name == "":
                # No Destination Folder is Browsed
                tmsg.showinfo("Error", "Please Browse a valid entry")
            else:
                ifExtractionSuccessful = DecryptData.extractBackUp(BackUp_File_Name, Destination_Folder_Name, Frame_3)

                clearWindow()
                Frame_1 = Frame()
                Frame_1.grid(row=0, column=0)
                Frame_2 = Frame()
                Frame_2.grid(row=1, column=0)
                if ifExtractionSuccessful:
                    # Extraction is successfully Complted
                    Label(Frame_1, text="Extraction is Successful", fg="green", font="Verdana 20 bold").grid(pady=10)
                    Button(Frame_2, text="Return To Main Page", bg="cyan", command=lambda: Home_Page()).grid(pady=10)
                else:
                    # Back Up is Failed due to some reason
                    Label(Frame_1, text="Extraction is Failed", fg="red", font="Verdana 20 bold").grid(pady=10)
                    Button(Frame_2, text="Return To Main Page", bg="cyan", command=lambda: Home_Page()).grid(pady=10)

Home_Page()
root.mainloop()