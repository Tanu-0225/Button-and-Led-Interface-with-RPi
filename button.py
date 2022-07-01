import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    buttonState = GPIO.input(16)
    if buttonState == False:
        GPIO.output(18,True)
        time.sleep(0.5)
        GPIO.output(18,False)
        time.sleep(0.5)
        print("Not Pressed")
    else:
        GPIO.output(18,GPIO.HIGH)
        print("Pressed")
