import RPi.GPIO as GP
from threading import Thread
import requests

GP.setmode(GP.BOARD)
GP.cleanup()
GP.setup(31, GP.IN)
GP.setup(32, GP.IN)
GP.setup(36, GP.OUT)
GP.output(36, GP.HIGH)

def joystick_loop():
    x = 0
    y = 0
    #counter = 0
    while True:
        #counter += 1
        #print("***", counter)
        if not GP.input(31):
            #print("x++")
            x += 1
        elif not GP.input(32):
            y += 1
        else:
            if x > 10 ** 5:
                #print("down")
                requests.post("http://localhost:5000/move/right")
            elif x > 10 ** 3:
                #print("up")
                requests.post("http://localhost:5000/move/left")

            if y > 10 ** 5:
                #print("left")# --> up
                requests.post("http://localhost:5000/move/up")
            elif y > 10 ** 3:
                #print("right") #--> down
                requests.post("http://localhost:5000/move/down")
             
            x, y = 0, 0

def start_controller():
	Thread(target = joystick_loop).start()