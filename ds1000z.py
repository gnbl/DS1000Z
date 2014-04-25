# -*- coding: utf-8 -*-

"""
Python script to save Rigol DS1000Z(-S) family oscilloscope screen to file ("screenshot", "hardcopy").
Should work with DS1074Z, DS1074Z-S, DS1104Z, DS1104Z-S.

Provided as is, no warranty, etc.

required Rigol instrument drivers http://int.rigol.com/prodserv/DS1000Z/software/
required NI VISA http://www.ni.com/visa/
required pyvisa https://pyvisa.readthedocs.org/
optional PILlow https://pillow.readthedocs.org/
"""


import sys
import io

try:
  import visa
except ImportError:
  print("pyVISA not installed")
  sys.exit()

  
def main():
  """
  pyVISA access needs to be encapsulated in function!? -> https://github.com/hgrecco/pyvisa/issues/33
  """
  rm = visa.ResourceManager()
  
  res = rm.list_resources()
  #print( res )
  ins = rm.get_instrument( res[0] ) # !
  
  '''
  idn = ins.ask("*IDN?")
  idns = idn.split(',')
  print( "Manufacturer:  ", idns[0] )
  print( "Device:     ", idns[1] )
  print( "Serial number:  ", idns[2] )
  print( "Firmware version:", idns[3] )
  '''
  
  ins.write(":DISP:DATA?")
  bmp = ins.read_raw()[2+9:]
  
  ins.close()
  
  # save image file
  filename = "screen"
  try:
    from PIL import Image
    print("Saving PNG")
    ext = ".png"
    im = Image.open( io.BytesIO(bmp) )
    im.save( filename + ext )
    
  except ImportError as e:
    print("PIL(low) not imported because:", e)
    print("Saving BMP")
    ext = ".bmp"
    with open( filename + ext , "wb") as f:
      f.write( bmp )


if __name__ == "__main__":

  print( "Python", sys.version, "on", sys.platform )
  print( "Pyvisa", visa.__version__ )
  
  main()
  
  print( "done." )

