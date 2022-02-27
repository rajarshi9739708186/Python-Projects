# pip install phonenumbers

from tkinter import *
import phonenumbers
import tkinter.messagebox as tmsg
from phonenumbers import geocoder, carrier, timezone

root = Tk()
root.geometry("800x500")
root.title("PhoneNumber Information")

def Home_Page(root):
    Frame_1 = Frame()
    Frame_1.grid(row=0, column=0)
    Frame_2 = Frame()
    Frame_2.grid(row=1, column=0)
    Frame_3 = Frame()
    Frame_3.grid(row=2, column=0)

    # Capture Phone Number
    # Phone Number must start with Country Code
    # +919739708186
    Label(Frame_1, text="Phone Number", padx=5, pady=2, font="Verdana 10 bold").grid(row=0, column=0)
    PhoneNumber = StringVar()
    Entry(Frame_1, width=35, textvariable=PhoneNumber).grid(row=0, column=1)
    Label(Frame_1, text="Enter Phone Number with Country Code", padx=5, pady=2, font="Verdana 7").grid(row=1, column=1)
    Label(Frame_1, text="PhoneNumber Example +919739708186", padx=5, pady=2, font="Verdana 7").grid(row=2, column=1)

    # Dispplay Information Field
    Label(Frame_2, text="Operator", padx=5, pady=5, font="Verdana 10 bold").grid(sticky="W", row=0, column=0)
    Operator_Info = Label(Frame_2, text="", fg="red", padx=5, pady=5, font="Verdana 10 bold")
    Operator_Info.grid(sticky="W", row=0, column=1)

    Label(Frame_2, text="Region  ", padx=5, pady=5, font="Verdana 10 bold").grid(sticky="W", row=1, column=0)
    Region_Info = Label(Frame_2, text="", fg="red", padx=5, pady=5, font="Verdana 10 bold")
    Region_Info.grid(sticky="W", row=1, column=1)

    Label(Frame_2, text="Timezone", padx=5, pady=5, font="Verdana 10 bold").grid(sticky="W", row=2, column=0)
    Timezone_Info = Label(Frame_2, text="", fg="red", padx=5, pady=5, font="Verdana 10 bold")
    Timezone_Info.grid(sticky="W", row=2, column=1)

    Button(Frame_3, text="Get Details", padx=10, bg="cyan", font="Verdana 10 bold", command=lambda: validatePhoneNumber(PhoneNumber.get().strip(), Operator_Info, Region_Info, Timezone_Info)).grid(sticky="W", pady=10)

def validatePhoneNumber(PhoneNumber, Operator_Info, Region_Info, Timezone_Info):
    try:
        PhoneNumber = phonenumbers.parse(PhoneNumber)
    except:
        # Phonenumber is blank
        # PhoneNumber doesn't start with Country code
        tmsg.showinfo("", "Phone Number is not valid")
        return

    # Wrong Phone Number
    if not phonenumbers.is_valid_number(PhoneNumber):
        tmsg.showinfo("", "Phone Number is not valid")
        return

    # Valid Phone Number
    # Get Phone Information
    operator, region, Phone_timezone = getPhoneDetails(PhoneNumber)

    # Display Phone Information
    displayPhoneDetails(operator, region, Phone_timezone, Operator_Info, Region_Info, Timezone_Info)

def getPhoneDetails(PhoneNumber):
    # Phone Operator
    try:
        operator = carrier.name_for_number(PhoneNumber, "en")
    except:
        operator = ""

    # Phone Region
    try:
        region = geocoder.description_for_number(PhoneNumber, "en")
    except:
        region = ""

    # Phone Time Zone
    try:
        Phone_timezone = timezone.time_zones_for_number(PhoneNumber)
    except:
        Phone_timezone = ""

    return operator, region, Phone_timezone

def displayPhoneDetails(operator, region, Phone_timezone, Operator_Info, Region_Info, Timezone_Info):
    if operator != "":
        Operator_Info["text"] = operator
    else:
        Operator_Info["text"] = ""

    if region != "":
        Region_Info["text"] = region
    else:
        Region_Info["text"] = ""

    if Phone_timezone != "":
        Timezone_Info["text"] = Phone_timezone
    else:
        Timezone_Info["text"] = ""

Home_Page(root)
root.mainloop()