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

lcd.clean()
