from netpbm import *

img = NetPBM()
img.load('P2.pgm')

print vars(img)

print 'Height: ' + str(img.height())
print 'Width: ' + str(img.width())
print 'Comment: ' + str(img.comment())

for color in img.export(ColorMap.b24):
	print hex(color)