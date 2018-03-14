import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
print "LOCK OPEN"
GPIO.output(23,GPIO.HIGH)
time.sleep(10)
print "Lock Closed"
GPIO.output(23, GPIO.LOW)
