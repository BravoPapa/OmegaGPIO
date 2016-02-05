from time import strftime
import omega_gpio

# Function to set RGB LED
def setrgb(red,green,blue):
  omega_gpio.setoutput(17,1 if red==0 else 0)
  omega_gpio.setoutput(16,1 if green==0 else 0)
  omega_gpio.setoutput(15,1 if blue==0 else 0)

######## Main routine starts here ########

#Initialize pins for RGB LED
for x in range(15,18):
  omega_gpio.initpin(x,'out')

#Start with the current time
curtime=strftime("%H%M%S")
newtime=curtime

# Infinite loop. 
while True:
  #Wait for time to change
  while newtime == curtime:
    newtime=strftime("%H%M%S")

  curtime=newtime

  #Set LED according to seconds
  seconds=int(curtime[-2:])
  ledtic=seconds % 6

  if seconds==59:
    setrgb(0,0,0) # off
  elif seconds==0:
    setrgb(1,1,1) # white
  elif ledtic==0:
    setrgb(1,0,0) # red
  elif ledtic==1:
    setrgb(0,1,0) # green
  elif ledtic==2:
    setrgb(0,0,1) # blue
  elif ledtic==3:
    setrgb(0,1,1) # cyan
  elif ledtic==4:
    setrgb(1,0,1) # magenta
  else:
    setrgb(1,1,0) # yellow

  R=1-omega_gpio.readinput(17)
  G=1-omega_gpio.readinput(16)
  B=1-omega_gpio.readinput(15)
  S=("R" if R==1 else " ") + ("G" if G==1 else " ") + ("B" if B==1 else " ")
  print S

# We'd like to see the dog kennels, please.

