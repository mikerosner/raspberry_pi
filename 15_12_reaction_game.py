import RPi.GPIO as GPIO ## Import GPIO library
import time

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.IN) ## Setup GPIO Pin 7 to IN
GPIO.setup(11, GPIO.IN) ## Setup GPIO Pin 11 to IN
winner = 0

## Sample light turn on code - GPIO.output(7,True) ## Turn on GPIO pin 7
## TBD turn on light for random 5-10 seconds
## Turn off light

if GPIO.input(7) :
    control1 = 1
else :
    control1 = 0
    
if GPIO.input(11) :
    control2 = 1
else :
    control2 = 0
    
try:
    while True:
        btn1 = GPIO.input(7)
        btn2 = GPIO.input(11)
        if control1 = 0 :
            if btn1 = 1 :
                winner = 1
                break
        else :
            if btn1 = 0 :
                control2 = 0 ## if button 1 is not pressed, assign control1 = 0
        
        if control2 = 0 :
            if btn2 = 1 :
                winner = 2
                break
        else :
            if btn2 = 0 :
                control2 = 0 ## if button 2 is not pressed, assign control2 = 0
        
        if reading :
            print "on"
        else : 
            print "off"
except KeyboardInterrupt:
    GPIO.cleanup()

print winner
sleep(5)
GPIO.cleanup()
