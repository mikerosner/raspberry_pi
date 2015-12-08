import RPi.GPIO as GPIO ## Import GPIO library
import time
import random
import lcd_class

lcd = lcd_class.lcd_data()

lcd.init()
temp_str = "Hello World!!!" ## 01000001
lcd.write_char(temp_str)
#print hex(0x200 + ord(temp_str[0]))

time.sleep(2)

lcd.clean()