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


def lcd_turn_on():
	GPIO.output(RS,False)
	GPIO.output(RW,False)	
	time.sleep(0.04)
	GPIO.output(E,1)
	time.sleep(0.04)	
	GPIO.output(DB0,1)
	GPIO.output(DB1,1)
	GPIO.output(DB2,1)
	GPIO.output(DB3,1)
	time.sleep(0.04)
	GPIO.output(E,0)	
	time.sleep(0.04)
	GPIO.output(DB0,0)
	GPIO.output(DB1,0)
	GPIO.output(DB2,0)
	GPIO.output(DB3,0)
 
def lcd_turn_off():
	GPIO.output(RS,False)
	GPIO.output(RW,False)	
	time.sleep(0.04)
	GPIO.output(E,1)
	time.sleep(0.04)	
	GPIO.output(DB0,0)
	GPIO.output(DB1,0)
	GPIO.output(DB2,0)
	GPIO.output(DB3,1)
	time.sleep(0.04)
	GPIO.output(E,0)	
	time.sleep(0.04)
	GPIO.output(DB3,0)

def lcd_init():
	GPIO.output(RS,False)
	GPIO.output(RW,False)	
	time.sleep(0.04)
	GPIO.output(E,1)
	time.sleep(0.04)	
	GPIO.output(DB5,1)
	GPIO.output(DB4,1)
	GPIO.output(DB3,1)
	GPIO.output(DB2,1)
	time.sleep(0.04)
	GPIO.output(E,0)	
	time.sleep(0.04)
	GPIO.output(DB5,0)
	GPIO.output(DB4,0)
	GPIO.output(DB3,0)
	GPIO.output(DB2,0)

lcd_init()
time.sleep(3)
lcd_turn_on()
time.sleep(3)
lcd_turn_off()

time.sleep(5)
GPIO.cleanup()
