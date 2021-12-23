import RPi.GPIO as GPIO
import time

LED_PIN = [4, 5, 6]
LED_NAME = ["red", "yellow", "green"]
GPIO.setmode(GPIO.BCM) #GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN[0], GPIO.OUT) #GPIO.OUT or GPIO.IN
GPIO.setup(LED_PIN[1], GPIO.OUT) #GPIO.OUT or GPIO.IN
GPIO.setup(LED_PIN[2], GPIO.OUT) #GPIO.OUT or GPIO.IN



for i in range(3):
    GPIO.output(LED_PIN[i], GPIO.HIGH) # 1
    print(LED_NAME[i])
    
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN[i], GPIO.LOW) # 0
    print(LED_NAME[i])
    print("led off")


GPIO.cleanup()