import RPi.GPIO as GPIO ## Import GPIO library
import time
import random
import lcd_class
import sys


lcd = lcd_class.lcd_data()

lcd.init()
d1 = {'line':1}
lcd.write_string(d1, sys.argv[1])
time.sleep(int(sys.argv[2]))
print lcd.get_line(1)

# initialize

# start main loop within try statement
try: do while 1 == 1:
	# if key pressed - act else don't
	if <key pressed down event>:
		KeyValue = <value of key pressed>
		
		# check for certain key presses:

		# backspace
		lcd.Backspace()

		# Enter
		lcd.ClearScreen()

		# Up Arrow
		lcd.MoveUp()

		# Down Arrow
		lcd.MoveDown()

		# Right
		lcd.MoveRight()

		# Left
		lcd.MoveLeft()

		# Insert
		if InsFlag == 1: InsFlag = 0
		else: InsFlag = 1

		# Try to print key to screen
		lcd.KeyPress(KeyValue, InsFlag)

# Except statement for main loop

		



lcd.clean()
