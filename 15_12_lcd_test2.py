import RPi.GPIO as GPIO ## Import GPIO library
import time
import random
import lcd_class

lcd = lcd_class.lcd_data()

lcd.init()
temp_str = "A"
lcd.write_char(temp_str)

time.sleep(2)
