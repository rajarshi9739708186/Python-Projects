import os
from tkinter import *
from tkinter import ttk
import sqlite3

def extractBackUp(BackUp_File_Name, Destination_Folder_Name, Frame_3):
    try:
        # Create SQLite connection
        sqliteConnection = sqlite3.connect(BackUp_File_Name)
        cursor = sqliteConnection.cursor()  # Using this object SQL query need to be executed

        # Get Row Count in table file_storage
        cursor.execute("select * from file_storage")
        rows_in_table = len(cursor.fetchall())

        # progress Bar
        Label(Frame_3, text="Extracting Back Up. Please wait ...", font="Verdana 10 bold").grid(padx=5, pady=5, row=0, column=0)
        progress_bar = ttk.Progressbar(Frame_3, orient=HORIZONTAL, length=500)
        progress_bar.grid(padx=5, pady=5, row=1, column=0)  # Placing Progress Bar on Screen
        progress_bar["maximum"] = rows_in_table

        # Convert Binary to File with proper Folder Structure
        progress_count = 0
        for record in cursor.execute("select * from file_storage"):
            progress_count += 1
            Relative_FileName = record[0]
            createFolderStructure(Relative_FileName, Destination_Folder_Name)
            ActualFileName = os.path.join(Destination_Folder_Name, Relative_FileName)
            Binary_to_File(record[1], ActualFileName)
            progress_bar["value"] = progress_count
            progress_bar.update()

        # Close Connection
        cursor.close()  # Close cursor object
        sqliteConnection.close()  # Terminate SQLite connection

        return True  # Extraction is Successful
    except:
        # Close Connection
        cursor.close()  # Close cursor object
        sqliteConnection.close()  # Terminate SQLite connection

        return False  # Extraction Failed

# Binary to File COnversion
def Binary_to_File(BinaryData, filename):
    with open(filename, "wb") as file:
        file.write(BinaryData)

# Create necessary Folder Structure
def createFolderStructure(Relative_FileName, Destination_Folder_Name):
    Folders = Relative_FileName.split("\\")
    Folders.pop()

    for Folder in Folders:
        Destination_Folder_Name = os.path.join(Destination_Folder_Name, Folder)
        if not os.path.exists(Destination_Folder_Name):
            os.mkdir(Destination_Folder_Name)