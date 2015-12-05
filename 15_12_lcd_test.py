import RPi.GPIO as GPIO ## Import GPIO library
import time
import random


RS = 24
RW = 26
E = 29
DB0 = 31
DB1 = 32
DB2 = 33
DB3 = 35
DB4 = 36
DB5 = 37
DB6 = 38
DB7 = 40
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

def lcd_turn_on:
  GPIO.setup(RS, GPIO.OUT)
  GPIO.setup(RW, GPIO.OUT)
  GPIO.setup(E, GPIO.OUT)
  GPIO.setup(DB0, GPIO.OUT)
  GPIO.setup(DB1, GPIO.OUT)
  GPIO.setup(DB2, GPIO.OUT)
  GPIO.setup(DB3, GPIO.OUT)
  GPIO.setup(DB4, GPIO.OUT)
  GPIO.setup(DB5, GPIO.OUT)
  GPIO.setup(DB6, GPIO.OUT)
  GPIO.setup(DB7, GPIO.OUT)
  
  GPIO.OUTPUT(RS,False)
  GPIO.OUTPUT(RW,False)
  GPIO.OUTPUT(E,True)
  GPIO.OUTPUT(E,True)
  
  

red_led = 12
ylw_led = 13
grn_led = 15
ply_1 = 7
ply_2 = 11


GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(ylw_led, GPIO.OUT)
GPIO.setup(grn_led, GPIO.OUT)
 
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
print "Player # " + str(winner) + " is the winner!"
time.sleep(5)
GPIO.cleanup()
