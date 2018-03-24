# import sys
# sys.path.append('../netpbm')
# from __init__ import *
from netpbm import *

print('Begin test...')
print('Load P1...')
img = NetPBM()
img.load('P1.pbm')

print('Height: ' + str(img.height()))
print('Width: ' + str(img.width()))
print('Comment: ' + str(img.comment()))

for color in img.export(ColorMap.b24):
	print(hex(color))

print('Load P2...')
img = NetPBM()
img.load('P2.pgm')

print('Height: ' + str(img.height()))
print('Width: ' + str(img.width()))
print('Comment: ' + str(img.comment()))

for color in img.export(ColorMap.b24):
	print(hex(color))

print('Load P3...')
img = NetPBM()
img.load('P3.ppm')

print('Height: ' + str(img.height()))
print('Width: ' + str(img.width()))
print('Comment: ' + str(img.comment()))

for color in img.export(ColorMap.b24):
	print(hex(color))

print('Load P4...')
img = NetPBM()
img.load('P4.pbm')

print('Height: ' + str(img.height()))
print('Width: ' + str(img.width()))
print('Comment: ' + str(img.comment()))

for color in img.export(ColorMap.b24):
	print(hex(color))

print('Load P5...')
img = NetPBM()
img.load('P5.pgm')

print('Height: ' + str(img.height()))
print('Width: ' + str(img.width()))
print('Comment: ' + str(img.comment()))

for color in img.export(ColorMap.b24):
	print(hex(color))

print('Load P6...')
img = NetPBM()
img.load('P6.ppm')

print('Height: ' + str(img.height()))
print('Width: ' + str(img.width()))
print('Comment: ' + str(img.comment()))

for color in img.export(ColorMap.b24):
	print(hex(color))