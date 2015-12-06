import RPi.GPIO as GPIO ## Import GPIO library
import ctypes
import time

c_uint8 = ctypes.c_uint8
class lcd_data_bits( ctypes.LittleEndianStructure ):
  _fields_ = [
    ("db0", c_uint8, 1 ),  # asByte & 512
    ("db1", c_uint8, 1 ),  # asByte & 256
    ("db2", c_uint8, 1 ),  # asByte & 128
    ("db3", c_uint8, 1 ),  # asByte & 64
    ("db4", c_uint8, 1 ),  # asByte & 32
    ("db5", c_uint8, 1 ),  # asByte & 16
    ("db6", c_uint8, 1 ),  # asByte & 8
    ("db7", c_uint8, 1 ),  # asByte & 4
    ("rw",  c_uint8, 1 ),  # asByte & 2
    ("rs",  c_uint8, 1 ),  # asByte & 1
  ]
  
class lcd_data( ctypes.Union ):
  _fields_ = [
    ("b",      lcd_data_bits ),
    ("asByte", c_uint8    )
  ]
  
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
  
  def lcd_load_db():
  	GPIO.output(self.DB0,self.b.db0)
  	GPIO.output(self.DB1,self.b.db1)
  	GPIO.output(self.DB2,self.b.db2)
  	GPIO.output(self.DB3,self.b.db3)
  	GPIO.output(self.DB4,self.b.db4)
  	GPIO.output(self.DB5,self.b.db5)
  	GPIO.output(self.DB6,self.b.db6)
  	GPIO.output(self.DB7,self.b.db7)
  	
  def write_cmd():
    GPIO.output(self.RS,self.b.rs)
    GPIO.output(self.RW,self.b.rw)
    GPIO.output(self.E,1)
    self.lcd_load_db()
    GPIO.output(self.E,0)
    sleep(0.001)
  
  def clear_dsp()
    self.asByte=0x001
    self.write_cmd()
    
  def rtrn_hme()
    self.asByte=0x002
    self.write_cmd()
    
  def funct_set(bool DL, bool N, bool F)
    self.asByte=0x03C
    self.write_cmd()
    
  def turn_on(bool D, bool C, bool B)
    self.asByte=0x00F
    self.write_cmd()
    
  def write_char(str x)
    self.asByte= 0x300 + x[1]
    self.write_cmd()
  
  def init()
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
    self.clear_dsp()
    self.rtrn_hme()
    self.turn_on(1,1,1)
    self.funct_set(1,1,1)
    
  def clean()
    self.clear_dsp()
    self.rtrn_hme()
    GPIO.cleanup()
    
_anonymous_ = ("b")
