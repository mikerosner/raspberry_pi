import RPi.GPIO as GPIO ## Import GPIO library
import time
import random
import lcd_class

lcd = lcd_class.lcd_data()

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

def lcd_load_db():
	GPIO.output(DB0,lcd.b.db0)
	GPIO.output(DB1,lcd.b.db1)
	GPIO.output(DB2,lcd.b.db2)
	GPIO.output(DB3,lcd.b.db3)
	GPIO.output(DB4,lcd.b.db4)
	GPIO.output(DB5,lcd.b.db5)
	GPIO.output(DB6,lcd.b.db6)
	GPIO.output(DB7,lcd.b.db7)

def lcd_load_char():
	lcd.asByte =0x241 ## 0x1001000001
	GPIO.output(RS,1)
	GPIO.output(RW,0)
	time.sleep(0.04)
	GPIO.output(E,1)
	time.sleep(0.04)
	lcd_load_db()
	time.sleep(0.04)
	GPIO.output(E,0)
	time.sleep(0.04)
	lcd.asByte = 0x000
	lcd_load_db()

def lcd_move_home():
	lcd.asByte =0x002 ## 0x0000000010
	GPIO.output(RS,0)
	GPIO.output(RW,0)
	time.sleep(0.04)
	GPIO.output(E,1)
	time.sleep(0.04)
	lcd_load_db()
	time.sleep(0.04)
	GPIO.output(E,0)
	time.sleep(0.04)
	lcd.asByte = 0x000
	lcd_load_db()

def lcd_clear_disp():
	lcd.asByte =0x001 ## 0x0000000010
	GPIO.output(RS,0)
	GPIO.output(RW,0)
	time.sleep(0.04)
	GPIO.output(E,1)
	time.sleep(0.04)
	lcd_load_db()
	time.sleep(0.04)
	GPIO.output(E,0)
	time.sleep(0.04)
	lcd.asByte = 0x000
	lcd_load_db()

lcd_init()
time.sleep(2)
lcd_turn_on()
time.sleep(2)
lcd_move_home()
lcd_load_char()
lcd_load_char()
lcd_load_char()
time.sleep(2)
lcd_clear_disp()
GPIO.cleanup()
