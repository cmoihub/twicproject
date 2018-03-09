import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

#def green_light:

#print "This is a test code for the LED "
#print"The green LED will turn on"
GPIO.output(24,GPIO.HIGH)
#print"Delaying for 5 seconds"
time.sleep(5)
#print "Now we turn it off"
GPIO.output(24,GPIO.LOW)
#print"The red LED will turn on"
#GPIO.output(23,GPIO.HIGH)
#print"Delaying for 5 seconds"
#time.sleep(5)
#print "Now we turn it off"
#GPIO.output(23,GPIO.LOW)