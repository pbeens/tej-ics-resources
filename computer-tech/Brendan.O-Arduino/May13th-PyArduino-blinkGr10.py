from pyfirmata import Arduino, util
from pyfirmata.util import Iterator
import time

pin=13 #pin to turn on = output
port='com14'    #read from Arduino IDE under Tools Port --> Com NOT '1'

board=Arduino(port)
iterator=Iterator(board)
iterator.start()

pin12=board.get_pin('d:12:i')#pin turn on = 5 volts/ off grd
pin12.enable_reporting

while True: #run endlessly...
    x=pin12.read() #get pin value
    print x        #check pin value
    
    if x:#true...
        print "pin12 on"
        board.digital[pin].write(1)
        time.sleep(0.9)
    else:#false...
        print "pin12 off"
        board.digital[pin].write(0)
        time.sleep(0.9)

board.exit()
