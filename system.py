import os
import time
import threading
import database as db


##--    ping db that system is online   --##
def pingDB():
    while True:
        db.RASPI_online()
        time.sleep(1)

        

t3 = threading.Thread(target=pingDB)
t3.start()


##--    start system                    --##

time.sleep(3)

db.motion_detectedRESET()
time.sleep(3)

while True:
    os.system("python3 cameraHTTP.py")
    time.sleep(10)
