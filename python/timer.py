from time import time, sleep
while True:
    sleep(30 - time() % 30)
    print("Hi")
