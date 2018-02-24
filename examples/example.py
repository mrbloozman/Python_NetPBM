# import sys
# sys.path.append('../netpbm')
# from __init__ import *
from netpbm import *

img = NetPBM()
img.load('P1.pbm')

print 'Height: ' + str(img.height())
print 'Width: ' + str(img.width())
print 'Comment: ' + str(img.comment())

for color in img.export(ColorMap.b24):
	print hex(color)

img = NetPBM()
img.load('P2.pgm')

print 'Height: ' + str(img.height())
print 'Width: ' + str(img.width())
print 'Comment: ' + str(img.comment())

for color in img.export(ColorMap.b24):
	print hex(color)

img = NetPBM()
img.load('P3.ppm')

print 'Height: ' + str(img.height())
print 'Width: ' + str(img.width())
print 'Comment: ' + str(img.comment())

for color in img.export(ColorMap.b24):
	print hex(color)

img = NetPBM()
img.load('P4.pbm')

print 'Height: ' + str(img.height())
print 'Width: ' + str(img.width())
print 'Comment: ' + str(img.comment())

for color in img.export(ColorMap.b24):
	print hex(color)

img = NetPBM()
img.load('P5.pgm')

print 'Height: ' + str(img.height())
print 'Width: ' + str(img.width())
print 'Comment: ' + str(img.comment())

for color in img.export(ColorMap.b24):
	print hex(color)

img = NetPBM()
img.load('P6.ppm')

print 'Height: ' + str(img.height())
print 'Width: ' + str(img.width())
print 'Comment: ' + str(img.comment())

for color in img.export(ColorMap.b24):
	print hex(color)