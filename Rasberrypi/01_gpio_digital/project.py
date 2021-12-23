import RPi.GPIO as GPIO 
import time 

LED_PIN = 3 # led 핀을 3으로 정해준다
SERVO_PIN = 18 # SERVO 핀을 18으로 정해준다
BUTTON_PIN = 8 # BUTTON 핀을 8으로 정해준다
BUZZER_PIN = 4 # BUZZER 핀을 4으로 정해준다

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 50)
GPIO.output(LED_PIN, False) #LED는 꺼져있는 상태이다.
try:
    while True:
        min = GPIO.input(BUTTON_PIN) #버튼이 눌렸는지 안눌렸는지 확인
        if min == GPIO.HIGH: #만약 버튼이 클릭 되었다면
            cmq = input("비밀번호를 입력해주세요") #cmq를 통해 비밀번호를 받아준다
            if cmq == "100": #만약 cmq와 정해져있는 비밀번호가 같다면
                pwm.start(2.5) #서보모터를 실행시켜준다
                GPIO.output(LED_PIN, True) #LED를 킨다
                print("비밀번호 확인")#비밀번호가 확인되었으므로 
                print("어서오세요 윤민님") #문이열렸다고 말해준다
                time.sleep(2) #2초 기다린후 
                break #함수를 빠져나온다
            else:
                p = GPIO.PWM(BUZZER_PIN, 262) #부저의 값을 넣어준다
                p.start(50) #부저를 실행시킨다
                print("잘못된 비밀번호입니다.") #비밀번호가 틀리다면
                time.sleep(2) #2초 기다린후 
                break #함수를 빠져나온다
        else:
            print("버튼 클릭없음") #비밀번호가 틀리다면 버튼 클릭 없음을 보낸다
finally:
    GPIO.output(LED_PIN, False)
    pwm.stop()
    GPIO.cleanup()
    