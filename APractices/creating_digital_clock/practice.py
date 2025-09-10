import datetime
import time
# while True:
#     now = datetime.now()
#     formatted = now.strftime("%d-%m-%Y, %H:%M:%S")
#     # print(formatted, end="\r", flush=True)  # Added flush=True
#     time.sleep(1)


# solution
while True:
    now = datetime.datetime.now()
    print(f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}", end="\r")
    time.sleep(1)
