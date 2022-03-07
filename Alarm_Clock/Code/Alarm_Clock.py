from tkinter import *
import datetime
import os

root = Tk()
root.geometry("600x300")
root.resizable(0, 0)
root.title("Alarm Clock")

Alarm_Time = ""
CurrentAlarm_Status = False

def Set_Alarm_Status():
    global CurrentAlarm_Status
    global Alarm_Time

    if CurrentAlarm_Status:
        # If Alarm button is on, It will be turned Off
        CurrentAlarm_Status = False
        alarm_deactivated()
    else:
        # If Alarm Button is Off, it will be turned on
        CurrentAlarm_Status = True
        # It will get time alarm time, which we set
        Alarm_Time = getAlarmTime(Hour_Clicked.get(), Minute_Clicked.get(), Second_Clicked.get(), AMorPM_Clicked.get())
        alarm_activated()

def alarm_activated():
    # Activate Alarm
    Alarm_button.config(text='Alarm Off', bg="red")
    # Once alarm is on, it should continously check System time
    check_system_time_continuously()

def alarm_deactivated():
    # Deactivate Alarm
    Alarm_button.config(text='Alarm On', bg="green")

def getAlarmTime(Hour, Minute, Second, AMorPM):
    Hour = int(Hour)
    Minute = int(Minute)
    Second = int(Second)

    if AMorPM == "PM":
        if Hour != 12:
            Hour += 12
    if AMorPM == "AM":
        if Hour == 12:
            Hour = 0

    return str(Hour)+":"+str(Minute)+":"+str(Second)

def check_system_time_continuously():
    global CurrentAlarm_Status
    global Alarm_Time

    # This block will be working, until Alarm is set to On
    if CurrentAlarm_Status:
        hour = int(datetime.datetime.now().hour)
        minute = int(datetime.datetime.now().minute)
        second = int(datetime.datetime.now().second)

        # Collect System Time
        current_system_time = str(hour)+":"+str(minute)+":"+str(second)

        # System TIme matches witj Alarm time
        if Alarm_Time == current_system_time:
            # It will open below mentioned Sound file
            os.startfile(os.path.join(os.getcwd(), "Sound_Mp3\\mixkit-spaceship-alarm-998.wav"))
            # Once Alarm sound started it will destroy GUI window
            root.destroy()

        # Recursively calling this fuction to check System time after each 1 second
        arbitary_label.after(1000, check_system_time_continuously)


frame_1 = Frame()
frame_1.grid(row=0, column=0)
frame_2 = Frame()
frame_2.grid(row=1, column=0)

# Hour
Hour_label = Label(frame_1, text='Hours', font="verdana 10 bold")
Hour_label.grid(padx=5, pady=15,row=0, column=0)

Hour_Options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
Hour_Clicked = StringVar()
Hour_Clicked.set(Hour_Options[0])
Hour_Dropdown = OptionMenu(frame_1, Hour_Clicked, *Hour_Options)
Hour_Dropdown.grid(row=0, column=1)

# Minutes
Minute_label = Label(frame_1, text='Minute', font="verdana 10 bold")
Minute_label.grid(padx=5, pady=15,row=0, column=2)

Minute_Options = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]
Minute_Clicked = StringVar()
Minute_Clicked.set(Minute_Options[0])
Minute_Dropdown = OptionMenu(frame_1, Minute_Clicked, *Minute_Options)
Minute_Dropdown.grid(row=0, column=3)

# Second
Second_label = Label(frame_1, text='Seconds', font="verdana 10 bold")
Second_label.grid(padx=5, pady=15,row=0, column=4)

Second_Options = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]
Second_Clicked = StringVar()
Second_Clicked.set(Second_Options[0])
Second_Dropdown = OptionMenu(frame_1, Second_Clicked, *Second_Options)
Second_Dropdown.grid(row=0, column=5)

# AM/PM
AMorPM_label = Label(frame_1, text='Period', font="verdana 10 bold")
AMorPM_label.grid(padx=5, pady=15,row=0, column=6)

AMorPM_Options = ["AM", "PM"]
AMorPM_Clicked = StringVar()
AMorPM_Clicked.set(AMorPM_Options[0])
AMorPM_Dropdown = OptionMenu(frame_1, AMorPM_Clicked, *AMorPM_Options)
AMorPM_Dropdown.grid(row=0, column=7)

Alarm_button = Button(frame_2, text='Alarm On', bg="green", padx=30, font="verdana 10 bold", command=Set_Alarm_Status)
Alarm_button.grid(pady = 15, row=0, column=0)

arbitary_label = Label(frame_2, text='')
arbitary_label.grid()

root.mainloop()