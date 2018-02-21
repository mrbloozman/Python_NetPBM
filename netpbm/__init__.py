class NetPBM:
   def __init__(self):
      self._magicNumber = None
      self._comment = ''
      self._width = None
      self._height = None
      self._maxColor = None
      self._src = []
      self._colorMap = {}

   def header(self):
      if not self._magicNumber:
         return True
      elif not self._width:
         return True
      elif not self._maxColor and self.maxColorRequired():
         return True
      else:
         return False

   def load(self,filepath):
      ba = []
      with open(filepath,'rb') as f:
         while self.header():
            ln = self.readLine(f)
            if not self._magicNumber:
               if ln in ['P1','P2','P3','P4','P5','P6']:
                  self._magicNumber = ln
               else:
                  raise IOError('NetPBM: Could not determine magic number')
            elif ln[0]=='#':
               self._comment = self._comment + str(ln)
            elif not self._width:
               props = ln.split()
               if len(props) >= 2:
                  self._width = int(props[0])
                  self._height = int(props[1])
               if len(props) == 3:
                  self._maxColor = int(props[2])
            elif not self._maxColor and self.maxColorRequired():
               props = ln.split()
               if len(props) == 1:
                  self._maxColor = int(props[0])
               else:
                  raise IOError('NetPBM: Could not find max color')

               
         # at this point we're reading either ascii or binary

         if self.isBitMap():
            self.srcBitMap(f)
         elif self.isGrayMap():
            self.srcGrayMap(f)
            self.setGrayMap565bit()
         elif self.isPixMap():
            self.srcPixMap(f)
            self.setColorMap565bit()


         # print vars(self)
         self.validate()

   def readLine(self,f):
      b = ''
      ln = ''
      while b != '\n':
         b = f.read(1)
         if b != '\n':
            ln = ln+b
         if b == '':
            return ln
      return ln

   def readBinary(self,f):
      ba = []
      b = f.read(1)
      while b != '':
         ba.append(b)
         b = f.read(1)
      return ba


   def srcBitMap(self,f):
      self._colorMap = {0:0,1:0}
      if self.isAscii():
         ln = self.readLine(f)
         while ln != '':
            for px in ln.strip().split():
               if px in ['0','1']:
                  self._src.append(int(px))
            ln = self.readLine(f)
      elif self.isBinary():
         bytewidth = (self._width+7)/8
         row = f.read(bytewidth)
         while len(row) > 0:
            bits=0
            for b in row:
               for i in range(8):
                  if bits < self._width:
                     self._src.append(b&(1<<i))
                     bits = bits+1
            row = f.readLine(bytewidth)

   def srcGrayMap(self,f):
      if self.isAscii():
         ln = self.readLine(f)
         while ln != '':
            for px in ln.strip().split():
               try:
                  ipx = int(px)
                  if ipx not in self._colorMap:
                     self._colorMap[ipx] = 0
                  self._src.append(ipx)
               except ValueError as e:
                  pass
            ln = self.readLine(f)
      elif self.isBinary():
         bytewidth = self._width
         row = f.read(bytewidth)
         while len(row) > 0:
            for px in row:
               ipx = ord(px)
               if ipx not in self._colorMap:
                  self._colorMap[ipx] = 0
               self._src.append(ipx)
            row = f.read(bytewidth)

   def srcPixMap(self,f):
      if self.isAscii():
         ln = self.readLine(f)
         while ln != '':
            pxs = ln.strip().split()
            for i in range(0,len(pxs),3):
               rpx = int(pxs[i])
               gpx = int(pxs[i+1])
               bpx = int(pxs[i+2])
               rgb = (rpx<<16)+(gpx<<8)+bpx
               if rgb not in self._colorMap:
                  self._colorMap[rgb] = 0
               self._src.append(rgb)
      elif self.isBinary():
         bytewidth = self._width*3
         row = f.read(bytewidth)
         while len(row) > 0:
            # pxs = bytes(ln)
            # print len(pxs)
            for i in range(0,bytewidth,3):
               # print pxs[i]
               rpx = ord(row[i])
               gpx = ord(row[i+1])
               bpx = ord(row[i+2])
               rgb = (rpx<<16)+(gpx<<8)+bpx
               if rgb not in self._colorMap:
                  self._colorMap[rgb] = 0
               self._src.append(rgb)
            row = f.read(bytewidth)

   def setColorMap24bit(self):
      for c in self._colorMap.keys():
         r = (c & 0xFF0000)>>16
         g = (c & 0xFF00)>>8
         b = (c & 0xFF)
         self._colorMap[c]=(self.normalizeColor(r,8)<<16)+(self.normalizeColor(g,8)<<8)+self.normalizeColor(b,8)

   def setColorMap565bit(self):
      for c in self._colorMap.keys():
         r = (c & 0xFF0000)>>16
         g = (c & 0xFF00)>>8
         b = (c & 0xFF)
         self._colorMap[c]=(self.normalizeColor(r,5)<<11)+(self.normalizeColor(g,6)<<5)+self.normalizeColor(b,5)

   def setGrayMap24bit(self):
      for c in self._colorMap.keys():
         g = self.normalizeColor(g,8)
         self._colorMap[c]=(g<<16)+(g<<8)+g

   def setGrayMap565bit(self):
      for c in self._colorMap.keys():
         g5 = self.normalizeColor(c,5)
         g6 = self.normalizeColor(c,6)
         self._colorMap[c]=(g5<<11)+(g6<<5)+g5

   def normalizeColor(self,c,bits):
      size = (1<<bits)-1
      # return size-int(size*c/self._maxColor)
      return int(size*c/self._maxColor)

   def validate(self):
      if (self._width * self._height) != len(self._src):
         raise IOError('NetPBM: Load is not valid')

   def export(self):
      data = []
      for px in self._src:
         data.append(self._colorMap[px])
      return data

   def maxColorRequired(self):
      if self._magicNumber in ['P2','P3','P5','P6']:
         return True
      else:
         return False

   def isAscii(self):
      if self._magicNumber in ['P1','P2','P3']:
         return True
      else:
         return False

   def isBinary(self):
      if self._magicNumber in ['P4','P5','P6']:
         return True
      else:
         return False

   def isBitMap(self):
      if self._magicNumber in ['P1','P4']:
         return True
      else:
         return False

   def isGrayMap(self):
      if self._magicNumber in ['P2','P5']:
         return True
      else:
         return False

   def isPixMap(self):
      if self._magicNumber in ['P3','P6']:
         return True
      else:
         return False

def bitSwap(b):
	x = 0b00000000
	for i in range(8):
		if (b&(1<<i)):
			x+=(128>>i)
	return x

def bitSwapList(l):
	i=0
	for f in l:
		newpic=[]
		for b in f:
			newpic.append(bitSwap(b))
		l[i]=newpic
		i+=1
	return l