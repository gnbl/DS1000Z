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

# standard library
import sys
import datetime

# pyvisa
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
  name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  print("Enter a filename-safe description (or none). Hit return.")
  comment = input( name + '_' )
  if( len(comment) ):
    name = name + "_" + comment
  try:
    from PIL import Image
    import io
    ext = ".png"
    filename = name + ext
    print("Saving screen as ", filename)
    im = Image.open( io.BytesIO(bmp) )
    im.save( filename )
    
  except ImportError as e:
    print("PIL(low) not imported because:", e)
    ext = ".bmp"
    filename = name + ext
    print("Saving screen as ", filename)
    with open( filename + ext , "wb") as f:
      f.write( bmp )


if __name__ == "__main__":
  
  print( "Python", sys.version, "on", sys.platform )
  print( "Pyvisa", visa.__version__ )
  
  main()
  
  print( "done." )

