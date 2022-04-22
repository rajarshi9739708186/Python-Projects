import sqlite3
from tkinter import *
from tkinter import ttk

def takeBackUp(File_List, BackUp_FileName, ifFileBackUp, File_or_Folder_Name, Frame_3):
    try:
        # Create SQLite connection
        sqliteConnection = sqlite3.connect(BackUp_FileName)
        cursor = sqliteConnection.cursor()  # Using this object SQL query need to be executed

        # Create Table to Capture File Name and File Data
        # Table Name : file_storage
        cursor.execute("create table file_storage (file_name char(100), actual_file blob)")  # Blob used for big information

        # progress Bar
        Label(Frame_3, text="Capturing Back Up. Please wait ...", font="Verdana 10 bold").grid(padx=5, pady=5, row=0, column=0)
        progress_bar = ttk.Progressbar(Frame_3, orient=HORIZONTAL, length=500)
        progress_bar.grid(padx=5, pady=5, row=1, column=0)  # Placing Progress Bar on Screen
        progress_bar["maximum"] = len(File_List)

        progress_count = 0
        if ifFileBackUp:
            # If it is a Single File Back Up
            # Capture Only File Name
            # Capture Binary Data for File
            for File_Name in File_List:
                progress_count += 1
                binary_obj = File_to_Binary(File_Name) # Convert Physical file into Binary
                sql_query = "insert into file_storage (file_name, actual_file) values (?, ?)" # Generate SQL Query
                data_tuple = (File_Name.split("\\")[-1], binary_obj) # Provide actual Data into SQL query
                cursor.execute(sql_query, data_tuple) # Execute SQL query
                progress_bar["value"] = progress_count
                progress_bar.update()
        else:
            # If it is a Folder Back Up
            # Capture relative File Name with Respect to Base Folder
            # Capture Binary Data for File
            for File_Name in File_List:
                progress_count += 1
                binary_obj = File_to_Binary(File_Name) # Convert Physical file into Binary
                sql_query = "insert into file_storage (file_name, actual_file) values (?, ?)" # Generate SQL Query
                data_tuple = (File_Name.replace(f"{File_or_Folder_Name}\\", ""), binary_obj) # Provide actual Data into SQL query
                cursor.execute(sql_query, data_tuple) # Execute SQL query
                progress_bar["value"] = progress_count
                progress_bar.update()

        # Commit SQL Update
        sqliteConnection.commit()

        # Close Connection
        cursor.close()  # Close cursor object
        sqliteConnection.close()  # Terminate SQLite connection

        return True # Successfully Took Back UP
    except:
        # Close Connection
        cursor.close()  # Close cursor object
        sqliteConnection.close()  # Terminate SQLite connection

        return False # Back Up Failed

# Convert Physical File into Binary Data
def File_to_Binary(filename):
    with open(filename, "rb") as file:
        blobdata = file.read()
    return blobdata
