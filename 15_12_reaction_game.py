import RPi.GPIO as GPIO ## Import GPIO library
import time

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.in) ## Setup GPIO Pin 7 to IN
GPIO.setup(11, GPIO.IN) ## Setup GPIO Pin 11 to IN

try:
    while True:
      GPIO.output(7,True) ## Turn on GPIO pin 7
      time.sleep(1) ## wait 1 second
      reading = GPIO.input(11) ## read pin 11
      if reading :
        print "on"
      else : 
        print "off"
except KeyboardInterrupt:
    GPIO.cleanup()
