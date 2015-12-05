import RPi.GPIO as GPIO ## Import GPIO library
import time
import random

red_led = 0
ylw_led = 0
grn_led = 0
ply_1 = 7
ply_2 = 11

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(ply_1, GPIO.IN) ## Setup GPIO Pin 7 to IN
GPIO.setup(ply_2, GPIO.IN) ## Setup GPIO Pin 11 to IN
winner = 0

print "Get Ready..."
GPIO.output(red_led,True)
time.sleep(2)
print "Get Set..."
GPIO.output(red_led,False)
GPIO.output(ylw_led,True)
time.sleep(random.uniform(3,5))
print "GO!"
print
GPIO.output(ylw_led,False)
GPIO.output(grn_led,True)

if GPIO.input(ply_1) :
    control1 = 0
else :
    control1 = 1

if GPIO.input(ply_2) :
    control2 = 0
else :
    control2 = 1

try:
    while True:
        btn1 = GPIO.input(ply_1)
        btn2 = GPIO.input(ply_2)
        if control1 == 0 :
            if btn1 == 0 :
                winner = 1
                break
        else :
            if btn1 == 1 :
                control1 = 0 ## if button 1 is not pressed, assign control1 = 0

        if control2 == 0 :
            if btn2 == 0 :
                winner = 2
                break
        else :
            if btn2 == 1 :
                control2 = 0 ## if button 2 is not pressed, assign control2 = 0

except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.output(grn_led,False)
print "Player # " + winner + " is the winner!"
time.sleep(5)
GPIO.cleanup()
