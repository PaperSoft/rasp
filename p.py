import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
print "start"
time.sleep(2)

GPIO.output(18,True)
print "power in"
time.sleep(2)

GPIO.cleanup()