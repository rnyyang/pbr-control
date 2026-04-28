import RPi.GPIO as GPIO
import time

RELAY = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY, GPIO.OUT)

# LED ON
GPIO.output(RELAY, 0)
print("LED ON")
time.sleep(5)

# LED OFF
GPIO.output(RELAY, 1)
print("LED OFF")

GPIO.cleanup()