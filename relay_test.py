import RPi.GPIO as GPIO
import time

RELAY = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY, GPIO.OUT)

# start OFF
GPIO.output(RELAY, 1)

print("OFF")
time.sleep(5)

print("ON")
GPIO.output(RELAY, 0)
time.sleep(5)

print("OFF")
GPIO.output(RELAY, 1)

GPIO.cleanup()