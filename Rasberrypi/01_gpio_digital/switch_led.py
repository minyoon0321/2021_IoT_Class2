import RPi.GPIO as GPIO
LED_PIN1 = 24
SWITCH_PIN1 = 4
LED_PIN2 = 12
SWITCH_PIN2 = 17
LED_PIN3 = 21
SWITCH_PIN3 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(SWITCH_PIN1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
try:
    while True:
        val = GPIO.input(SWITCH_PIN1)
        print(val)
        GPIO.output(LED_PIN1, val)
        val = GPIO.input(SWITCH_PIN2)
        print(val)
        GPIO.output(LED_PIN2, val)
        val = GPIO.input(SWITCH_PIN3)
        print(val)
        GPIO.output(LED_PIN3, val)
finally:
    GPIO.cleanup()
    print('cleanup and exit')