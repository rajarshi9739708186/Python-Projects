from tkinter import *

root = Tk()
root.geometry("600x300")
root.resizable(0, 0)
root.title("Stop Watch")

running = False
update_time =""
hours, minutes, seconds = 0, 0, 0

def start():
    global running
    if not running:
        update()
        running = True

def pause():
    global running

    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

def reset():
    global running

    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

    # set variables back to zero
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0

    # set label back to zero
    stopwatch_label.config(text='00:00:00')

def update():
    global hours, minutes, seconds
    global update_time

    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    if seconds > 9:
        seconds_string = str(seconds)
    else:
        seconds_string = f"0{seconds}"

    if minutes > 9:
        minutes_string = str(minutes)
    else:
        minutes_string = f"0{minutes}"

    if hours > 9:
        hours_string = str(hours)
    else:
        hours_string = f"0{hours}"

    stopwatch_label.config(text=f"{hours_string}:{minutes_string}:{seconds_string}")
    update_time = stopwatch_label.after(1000, update) # After 1 second call itself and update new time; 1000 ms => 1Second

frame_1 = Frame() # It will create a frame and object wuill be returned to frame_1
frame_1.grid(row=0, column=0) # Placing frmae_1 at ROW=0, COLUMN=0

frame_2 = Frame() # It will create a frame and object wuill be returned to frame_2
frame_2.grid(row=1, column=0) # Placing frmae_2 at ROW=1, COLUMN=0

stopwatch_label = Label(frame_1, text='00:00:00', font=('Arial', 80))
stopwatch_label.grid()

start_button = Button(frame_2, text='start', bg="cyan", padx=30, font="verdana 10 bold", command=start)
start_button.grid(padx=5, row=1, column=0)
pause_button = Button(frame_2, text='pause', bg="cyan", padx=30, font="verdana 10 bold", command=pause)
pause_button.grid(padx=5, row=1, column=1)
reset_button = Button(frame_2, text='reset', bg="cyan", padx=30, font="verdana 10 bold", command=reset)
reset_button.grid(padx=5, row=1, column=2)
quit_button = Button(frame_2, text='quit', bg="cyan",padx=30, font="verdana 10 bold", command=root.quit)
quit_button.grid(padx=5, row=1, column=3)

root.mainloop()