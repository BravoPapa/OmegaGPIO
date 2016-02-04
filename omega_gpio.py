# Paths to the GPIO filesystem
_exportpath = '/sys/class/gpio/gpiochip0/subsystem/export'
_unexportpath = '/sys/class/gpio/gpiochip0/subsystem/unexport'
_gpiopath = '/sys/class/gpio/gpio'

# Write to the GPIO fs. Seems to need to close to take effect
def writetofs(fname,data):
  f=open(fname,'w')
  f.write(data)
  f.close()

#Read from GPIO fs.
def readfromfs(fname):
  f=open(fname,'r')
  s=f.read()
  f.close()
  if s[0]=='1':
    v=1
  else:
    v=0
  return v

def readinput(pin):
  rdval=readfromfs(_gpiopath+str(pin)+'/value')
  return rdval

# "Export" the pin and set the direction
def initpin(pin,direction):
  writetofs(_exportpath,str(pin))
  writetofs(_gpiopath+str(pin)+'/direction',direction)

# Release the pin when done
def closepin(pin):
  writetofs(_unexportpath,str(pin))

# Set the output value. Write a 1 or 0 (numeric). Any non-zero value for high
def setoutput(pin,value):
  if value == 0:
    wrval='0'
  else:
    wrval='1'
  writetofs(_gpiopath+str(pin)+'/value',wrval)

