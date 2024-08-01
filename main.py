import time
import random
from pypresence import Presence

time.sleep(10)

client_id = "1268516316529033300"

rpc = Presence(client_id)
rpc.connect()


my_stack = [
    "Python - 1.5 years",
    "C++ - 6 month",
    "C# - 5 month"
]

in_time = time.time()

github_url = "https://github.com/solarezz"
tgc_url = "https://t.me/top1invokerinmyroom"
btns = [{"label": "My GitHub", "url": github_url}, {"label": "My TGc", "url": tgc_url}]

try:
    print("Подключение...")
    while True:
        rpc.update(
            details="My random stack:",
            state=random.choice(my_stack),
            start=in_time,
            buttons=btns,
            large_image = "maxdiscord",
            large_text = "Beginner Python Developer"
            )
        time.sleep(15)
except KeyboardInterrupt:
    print("Отключение...")
    rpc.close()

