import RPi.GPIO as GPIO
import time


# -- setup --
GPIO.setmode(GPIO.BCM)
# motors
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

# -- movement --
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.HIGH)
GPIO.output(16, GPIO.LOW)
GPIO.output(20, GPIO.HIGH)

time.sleep(5)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(20, GPIO.LOW)

GPIO.cleanup()
