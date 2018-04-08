Note: There's very likely better software out there, none tried but e.g. https://github.com/pklaus/ds1054z (connects via Ethernet, also has improved on the use of my mask images to darken unimportant areas of the screen, i.e. the logo etc.). The VISA stuff has always caused me some pain (very large software packages, connection issues) ...

DS1000Z
=======

Python script using pyVISA to grab a screenshot from Rigol DS1000Z oscilloscope


Dependencies
* required Rigol instrument drivers http://int.rigol.com/prodserv/DS1000Z/software/
* required NI VISA http://www.ni.com/visa/
* required pyvisa https://pyvisa.readthedocs.org/
* optional PILlow https://pillow.readthedocs.org/

Also see the script's header comment:
* https://github.com/gnbl/DS1000Z/blob/master/ds1000z.py
