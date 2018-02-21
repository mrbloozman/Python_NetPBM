from netpbm import NetPBM

img = NetPBM()
img.load('P2.pgm')
img.setGrayMap24bit()

print vars(img)

print 'Height: ' + str(img.height())
print 'Width: ' + str(img.width())
print 'Comment: ' + str(img.comment())

for color in img.export():
	print hex(color)