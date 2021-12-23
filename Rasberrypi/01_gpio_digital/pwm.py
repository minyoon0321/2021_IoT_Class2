import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [391, 391, 440, 440, 391, 391, 329]
melody2 = [391, 391, 329, 329, 293]
melody3 = [391, 329, 293, 329, 261]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.7)
    for i in melody2:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.7)
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.7)
    for i in melody3:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
        
finally:
    pwm.stop()
    GPIO.cleanup()