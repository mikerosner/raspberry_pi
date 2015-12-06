import ctypes

c_uint8 = ctypes.c_uint8
class lcd_data_bits( ctypes.LittleEndianStructure ):
  _fields_ = [
    ("db0"
    ("rw",  c_uint8, 1 ),  # asByte & 2
    ("db7", c_uint8, 1 ),  # asByte & 4
    ("db6", c_uint8, 1 ),  # asByte & 8
    ("db5", c_uint8, 1 ),  # asByte & 16
    ("db4", c_uint8, 1 ),  # asByte & 32
    ("db3", c_uint8, 1 ),  # asByte & 64
    ("db2", c_uint8, 1 ),  # asByte & 128
    ("db1", c_uint8, 1 ),  # asByte & 256
    ("db0", c_uint8, 1 ),  # asByte & 512
  ]
  
class lcd_data( ctypes.Union ):
  _fields_ = [
    ("b",      lcd_data_bits ),
    ("asByte", c_uint8    )
  ]
_anonymous_ = ("b")

lcd = lcd_data()
lcd.asByte = 0x4  # ->0100

print lcd.b.db0
print lcd.b.db1
print lcd.b.db2
print lcd.b.db3
print lcd.b.db4
print lcd.b.db5
print lcd.b.db6
print lcd.b.db7
print lcd.b.rw
print lcd.b.rs
