import RPi.GPIO as GPIO ## Import GPIO library
import ctypes
import time

c_uint16 = ctypes.c_uint16
class lcd_data_bits( ctypes.LittleEndianStructure ):
  _fields_ = [
    ("db0", c_uint16, 1 ),  # asByte & 
    ("db1", c_uint16, 1 ),  # asByte & 
    ("db2", c_uint16, 1 ),  # asByte & 
    ("db3", c_uint16, 1 ),  # asByte &
    ("db4", c_uint16, 1 ),  # asByte &
    ("db5", c_uint16, 1 ),  # asByte &
    ("db6", c_uint16, 1 ),  # asByte & 
    ("db7", c_uint16, 1 ),  # asByte & 
    ("rw",  c_uint16, 1 ),  # asByte & 
    ("rs",  c_uint16, 1 ),  # asByte & 
  ]
  
class lcd_data( ctypes.Union ):
  _fields_ = [
    ("b",      lcd_data_bits ),
    ("asByte", c_uint16    )
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
  
  ##Tier 0 Functions
  def GPIO_read_init(self):
  	GPIO.setup(self.DB0, GPIO.IN)
  	GPIO.setup(self.DB1, GPIO.IN)
  	GPIO.setup(self.DB2, GPIO.IN)
  	GPIO.setup(self.DB3, GPIO.IN)
  	GPIO.setup(self.DB4, GPIO.IN)
  	GPIO.setup(self.DB5, GPIO.IN)
  	GPIO.setup(self.DB6, GPIO.IN)
  	GPIO.setup(self.DB7, GPIO.IN)
  
  def GPIO_write_init(self):
  	GPIO.setup(self.DB0, GPIO.OUT)
  	GPIO.setup(self.DB1, GPIO.OUT)
  	GPIO.setup(self.DB2, GPIO.OUT)
  	GPIO.setup(self.DB3, GPIO.OUT)
  	GPIO.setup(self.DB4, GPIO.OUT)
  	GPIO.setup(self.DB5, GPIO.OUT)
  	GPIO.setup(self.DB6, GPIO.OUT)
  	GPIO.setup(self.DB7, GPIO.OUT)
  
  def lcd_load_db(self):
  	GPIO.output(self.DB0,self.b.db0)
  	GPIO.output(self.DB1,self.b.db1)
  	GPIO.output(self.DB2,self.b.db2)
  	GPIO.output(self.DB3,self.b.db3)
  	GPIO.output(self.DB4,self.b.db4)
  	GPIO.output(self.DB5,self.b.db5)
  	GPIO.output(self.DB6,self.b.db6)
  	GPIO.output(self.DB7,self.b.db7)
  	
  def printvars(self):
	print str(self.b.rs) + str(self.b.rw) + str(self.b.db7) + str(self.b.db6) + str(self.b.db5) + str(self.b.db4) + str(self.b.db3) + str(self.b.db2) + str(self.b.db1) + str(self.b.db0)
  
  def read_cmd(self):
  	GPIO.output(self.RS,self.b.rs)
  	GPIO.output(self.RW,self.b.rw)
  	self.GPIO_read_init()
  	GPIO.output(self.E,1)
  	self.b.db0 = GPIO.input(self.DB0)
  	self.b.db1 = GPIO.input(self.DB1)
  	self.b.db2 = GPIO.input(self.DB2)
  	self.b.db3 = GPIO.input(self.DB3)
  	self.b.db4 = GPIO.input(self.DB4)
  	self.b.db5 = GPIO.input(self.DB5)
  	self.b.db6 = GPIO.input(self.DB6)
  	self.b.db7 = GPIO.input(self.DB7)
  	GPIO.output(self.E,0)
  	self.GPIO_write_init()
  	##time.sleep(0.001)
  	
  def write_cmd(self):
  	x = 1
  	temp = self.asByte
  	while x == 1 :
  		self.asByte = 0x100
  		self.read_cmd()
  		x = self.b.db7
  	self.asByte = temp
  	GPIO.output(self.RS,self.b.rs)
  	GPIO.output(self.RW,self.b.rw)
  	GPIO.output(self.E,1)
  	self.lcd_load_db()
  	GPIO.output(self.E,0)
  	##time.sleep(0.001)
  	##self.printvars()
  
  def clear_dsp(self):
    self.asByte=0x001
    self.write_cmd()
    
  def rtrn_hme(self):
    self.asByte=0x002
    self.write_cmd()
    
  def funct_set(self,DL, N, F):
    self.asByte=0x03C
    self.write_cmd()
    
  def turn_on(self,D, C, B):
    self.asByte=0x00F
    self.write_cmd()
    
  def get_line(self,line_num):
  	##implementation tbd
  	return "not implemented"
  
  def mv_curs(self,addr):
  	##line1 - 0x00; line2 - 0x40
  	self.asByte= 0x80 + addr
  	self.write_cmd()
    
  def write_string(self,txt1,line_num):
    a1 = 0x200
    clr_scrn = "                 "
    if line_num == 1: addr = 0x00
    else: addr = 0x40
    self.mv_curs(addr)
    for i in clr_scrn:
    	self.asByte= a1 + ord(i) 
    	self.write_cmd()
    self.mv_curs(addr)
    for i in txt1:
    	self.asByte= a1 + ord(i) 
    	self.write_cmd()
		
  def init(self):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(self.RS, GPIO.OUT)
    GPIO.setup(self.RW, GPIO.OUT)
    GPIO.setup(self.E, GPIO.OUT)
    self.GPIO_write_init()
    self.clear_dsp()
    self.rtrn_hme()
    self.turn_on(1,1,1)
    self.funct_set(1,1,1)
    
  def clean(self):
    self.clear_dsp()
    self.rtrn_hme()
    GPIO.cleanup()
    
##_anonymous_ = ("b")
