from tkinter import *
import socket
import netifaces
import os
from getmac import get_mac_address
from datetime import datetime
from time import strftime
from PIL import Image, ImageTk

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    gws = netifaces.gateways()
    s.connect(("8.8.8.8", 80))
    user = socket.gethostname()
    mac_address = get_mac_address()
    ip = s.getsockname()[0]
    gateway = gws["default"][2][0]
except OSError:
    print("please check your connection!")
    user = "Check your connection!"
    mac_address = "Check your connection!"
    gateway = "Check your connection!"
    date = "Check your connection!"
    ip = "Check your connection!"

win = Tk()
win.geometry("500x350")
win.title("Red Support It")


def upd_time():
    string = strftime("%I:%M:%S %p")
    time_label.config(text=string)
    time_label.after(1000, upd_time)


image = Image.open("logo.png")
image = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = Label(win, image=image)
image_label.pack()


time_label = Label(win, font=("calibri", 14, "bold"))
time_label.pack()

com_name_title = Label(win, text=f"Computer name:", font=("calibri", 14))
com_name_title.pack()

com_name = Label(win, text=user, font=("calibri", 14, "bold"), bg="cyan")
com_name.pack()

ip_address_title = Label(win, text=f"IP address:", font=("calibri", 14))
ip_address_title.pack()

ip_address = Label(win, text=ip, font=("calibri", 14, "bold"), bg="red")
ip_address.pack()

gateway_address_title = Label(win, text=f"Gateway address:", font=("calibri", 14))
gateway_address_title.pack()

gateway_address = Label(win, text=gateway, font=("calibri", 14, "bold"), bg="yellow")
gateway_address.pack()

mac_address_title = Label(win, text=f"Mac address:", font=("calibri", 14))
mac_address_title.pack()

mac_address_label = Label(
    win, text=mac_address, font=("calibri", 14, "bold"), bg="lightgreen"
)
mac_address_label.pack()

upd_time()

win.mainloop()

s.close()
