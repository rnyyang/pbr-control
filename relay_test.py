import RPi.GPIO as GPIO
import time

RELAY = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY, GPIO.OUT)

print("Turning ON")
GPIO.output(RELAY, 0)
time.sleep(5)

print("Turning OFF")
GPIO.output(RELAY, 1)

GPIO.cleanup()