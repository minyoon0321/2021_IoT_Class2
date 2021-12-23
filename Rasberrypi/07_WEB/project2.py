#프로젝트 실행을 위한 모듈 
import time
from lcd import drivers 
import adafruit_ssd1306 
import board
import cv2
import digitalio
import RPi.GPIO as GPIO
import pigpio #서보모터가 떨리지 않도록 잡아주는 모듈
from flask import Flask, render_template, Response
import cv2

#GPIO핀 설정
SERVO_PIN = 18
TRIG_PIN = 4
ECHO_PIN = 14
BUZZER_PIN = 6
#GPIO모드 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
cap = cv2.VideoCapture(0)
pwm = GPIO.PWM(BUZZER_PIN, 330)
display = drivers.Lcd()
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm1 = GPIO.PWM(SERVO_PIN, 50)
pi = pigpio.pi()
pi.set_servo_pulsewidth(18, 500)
time.sleep(1)

if not cap. isOpened():
    print('Camera open failed')
    exit()

#Flask 객체 생성
#__name__은 파일명
app = Flask(__name__)
camera = cv2.VideoCapture(0)  # camera를 0으로 바꾸기

def gen_frames(): #카메라에 프레임 단위로 생성하는 함수
    while True:
        # 프레임별로 캡쳐
        success, frame = camera.read()  # 카메라 프레임 읽기
        if (not success):
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            print(frame)
                   # 프레임을 하나씩 연결하고 결과 보여주기 

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/') # 라우팅을 위한 뷰 함수
def index():
    return render_template('first.html')

if (__name__ == '__main__'): # 터미널에서 직접 실행시킨 경우
    try: 
        app.run(host='0.0.0.0', port=8080)
    finally:
        print("clean up")

try:
    while True:      
        #카메라 촬영하기
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) == 27:
            break
        #초음파 센서를 이용한 거리 측정
        GPIO.output(TRIG_PIN, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, False)
        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time()
        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time()
        
        #초음파의 시간차를 이용해 거리 측정하기
        duration_time = stop - start
        distance = duration_time*17160

        #거리가 30 이하라면...
        if distance < 30:
            print('Distance: %.1fcm' % distance) #연결된 컴퓨터에 거리 출력
            display.lcd_display_string("someone detected", 1) #LCD에 거리를 출력하고 누군가 감지되었음을 출력
            display.lcd_display_string('Distance: %.1fcm' % distance, 2)
            cv2.imwrite('stranger.jpg', frame) #사진 촬영
            pi.set_servo_pulsewidth(18, 1500) #서보 모터 회전을 통한 문 닫기
            time.sleep(1)
            pwm.start(50) #피에조 부저를 통해 감지되었음을 알린다
            time.sleep(5)
            pwm.stop()
            
finally:
    #장치 정리
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
    print('cleanup and exit')


