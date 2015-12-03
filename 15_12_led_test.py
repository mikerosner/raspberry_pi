import RPi.GPIO as GPIO ## Import GPIO library
from msvcrt import getch

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

while true : 
  key = ord(getch())
  GPIO.output(7,True) ## Turn on GPIO pin 7
  if key == 13: #Enter
    break
GPIO.cleanup()
