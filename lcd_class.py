import ctypes

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
_anonymous_ = ("b")


