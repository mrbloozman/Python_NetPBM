# Python_NetPBM
Provides NetPBM class to load .pbm, .pgm, or .ppm files

For a detailed description of NetPBM file formats, read https://en.wikipedia.org/wiki/Netpbm_format

## NetPBM()

Class constructor

## NetPBM.load(filepath)

str filepath = path to .pbm, .pgm, or .ppm file

Image files can be either ascii or binary types

## NetPBM.height()

int returns pixel height

## NetPBM.width()

int returns pixel width

## NetPBM.comment()

str returns comment if one exists in the loaded image file

## NetPBM.export(colorMap)

enum colorMap = either ColorMap.b16 (for 16bit colors values, 565 RGB) or ColorMap.b24 (for 24bit color values, 888 RGB)

int list returns pixel colors as 16bit or 24bit RGB values.  Will yield a list containing one integer per pixel of data (i.e. list will have width x height number of values).  Exported data is intended to be easily written to a display controller via serial protocol.
