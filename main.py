import time
import random
import os
import win32con
import win32console
import win32gui
import threading
from pypresence import Presence
from PIL import Image
from pystray import Icon, MenuItem, Menu
from pathlib import Path

client_id = "1268516316529033300"

shortcut = r"C:\Users\solarezz\AppData\Local\Discord\app-1.0.9158\Discord.exe"
os.startfile(shortcut)
time.sleep(20)

working = False

rpc = Presence(client_id)
rpc.connect()

def start_presence():
    my_stack = [
        "Python - 1.5 years",
        "C++ - 6 month",
        "C# - 5 month"
    ]

    in_time = time.time()

    github_url = "https://github.com/solarezz"
    tgc_url = "https://t.me/top1invokerinmyroom"
    btns = [{"label": "My GitHub", "url": github_url}, {"label": "My TGc", "url": tgc_url}]

    rpc.update(
        details="My stack:",
        state=my_stack[0],
        start=in_time,
        buttons=btns,
        large_image="maxdiscord",
        large_text="Beginner Python Developer",
        small_image="minpython",
        small_text="Python 3.12.4"
    )

def click(icon: Icon, item: MenuItem):
    icon.stop()

def updater():
    start_presence()
    time.sleep(15)

def main():
    image = Image.open(Path.cwd() / "pic" / "app.ico")
    icon = Icon('DRPC Script', image, menu=Menu(
            MenuItem('Выход', click)
        ))
    win32gui.ShowWindow(win32console.GetConsoleWindow(), win32con.SW_HIDE)
    icon.run()

try:
    rpc = Presence(client_id)
    rpc.connect()
    start_presence()
    print("Всё отлично работает!")
    time.sleep(3)
    while True:
        if not working:
            main()
            working = True
        start_presence()
        time.sleep(15)
except KeyboardInterrupt:
    print("Отключение...")
    rpc.close()
except:
    shortcut = r"C:\Users\solarezz\AppData\Local\Discord\app-1.0.9156\Discord.exe"
    os.startfile(shortcut)
    time.sleep(20)
    rpc = Presence(client_id)
    rpc.connect()
    start_presence()
    print("Всё отлично работает!")
    time.sleep(3)
    while True:
        if not working:
            main()
            working = True
        start_presence()
        time.sleep(15)
