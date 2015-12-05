import RPi.GPIO as GPIO ## Import GPIO library
import time
import random

red_led = 12
ylw_led = 13
grn_led = 15
ply_1 = 7
ply_2 = 11

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

def lcd_turn_on():
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
  
  GPIO.output(RS,False)
  GPIO.output(RW,False)
  GPIO.output(E,True)
  GPIO.output(DB0,True)
  GPIO.output(DB1,True)
  GPIO.output(DB2,True)
  GPIO.output(DB3,True)
  time.sleep(0.01)
  GPIO.output(E,False)
  time.sleep(0.01)
  GPIO.output(DB0,False)
  GPIO.output(DB1,False)
  GPIO.output(DB2,False)
  GPIO.output(DB3,False)
  
def lcd_turn_off():
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
  
  GPIO.output(RS,False)
  GPIO.output(RW,False)
  GPIO.output(E,True)
  GPIO.output(DB0,False)
  GPIO.output(DB1,False)
  GPIO.output(DB2,False)
  GPIO.output(DB3,True)
  time.sleep(0.01)
  GPIO.output(E,False)
  time.sleep(0.01)
  GPIO.output(DB3,False)

lcd_turn_on()
time.sleep(3)
lcd_turn_off()

time.sleep(5)
GPIO.cleanup()
