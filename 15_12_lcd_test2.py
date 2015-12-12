import RPi.GPIO as GPIO ## Import GPIO library
import time
import random
import lcd_class
import sys


lcd = lcd_class.lcd_data()

lcd.init()

lcd.parse_xml(sys.argv[1])

print lcd.get_line(1)

lcd.clean()
