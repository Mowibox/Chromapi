import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit


ANGLE_MIN = 0  
ANGLE_MAX = 180 

GPIO_LED_L = 23    
GPIO_LED_R = 22 

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_LED_L, GPIO.OUT)  
GPIO.setup(GPIO_LED_R, GPIO.OUT) 
GPIO.output(GPIO_LED_L, GPIO.LOW)
GPIO.output(GPIO_LED_R, GPIO.LOW)

NUM_OF_CHANNELS = 16

kit = ServoKit(channels=NUM_OF_CHANNELS)

def set_servo_angle(channel, angle):
    if 0 <= channel < 16 and 0 <= angle <= 180:
        kit.servo[channel].angle = angle
    else:
        print("Invalid value for channel or angle! channel must be between [0-15] and angle between [0-180].")

def move_all_servos():
        for angle in range(ANGLE_MIN, ANGLE_MAX):
            for channel in range(NUM_OF_CHANNELS):
                set_servo_angle(channel, angle)
            time.sleep(0.001) 

        for angle in range(ANGLE_MAX, ANGLE_MIN, -1):
            for channel in range(NUM_OF_CHANNELS):
                set_servo_angle(channel, angle)
            time.sleep(0.001) 

def servo_shutdown(channel):
    kit.servo[channel].angle = None

def shutdown_all_servos():
    for channel in range(NUM_OF_CHANNELS):
        servo_shutdown(channel)
    
if __name__ == "__main__":
    time.sleep(2)
    move_all_servos()
    shutdown_all_servos()
    set_servo_angle(10, 180)
    set_servo_angle(11, 180)
    set_servo_angle(3, 180)
    time.sleep(1)
    set_servo_angle(8, 90)
    set_servo_angle(9, 180)
    time.sleep(0.5)
    set_servo_angle(8, 0)
    set_servo_angle(9, 90)
    time.sleep(0.5)
    set_servo_angle(8, 90)
    set_servo_angle(9, 180)
    time.sleep(0.5)
    set_servo_angle(8, 0)
    set_servo_angle(9, 90)
    time.sleep(0.5)
    set_servo_angle(8, 90)
    set_servo_angle(9, 180)
    time.sleep(0.5)
    set_servo_angle(8, 0)
    set_servo_angle(9, 90)
    time.sleep(0.5)
    set_servo_angle(8, 45)
    set_servo_angle(9, 0)
    set_servo_angle(2, 180-45)
    time.sleep(1)
    shutdown_all_servos()
    time.sleep(0.5)
    for i in range(6):
        GPIO.output(GPIO_LED_L, GPIO.HIGH)
        GPIO.output(GPIO_LED_R, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(GPIO_LED_L, GPIO.LOW)
        GPIO.output(GPIO_LED_R, GPIO.LOW)
        time.sleep(0.3)
    time.sleep(35)
    set_servo_angle(8, 0)
    set_servo_angle(9, 90)
    set_servo_angle(2, 180)
    set_servo_angle(3, 90)
    time.sleep(0.5)
    set_servo_angle(8, 90)
    set_servo_angle(9, 180)
    set_servo_angle(2, 90)
    set_servo_angle(3, 0)
    time.sleep(0.5)
    set_servo_angle(8, 0)
    set_servo_angle(9, 90)
    set_servo_angle(2, 180)
    set_servo_angle(3, 90)
    time.sleep(0.5)
    set_servo_angle(8, 90)
    set_servo_angle(9, 180)
    set_servo_angle(2, 90)
    set_servo_angle(3, 0)
    time.sleep(0.5)
    set_servo_angle(8, 0)
    set_servo_angle(9, 90)
    set_servo_angle(2, 180)
    set_servo_angle(3, 90)
    time.sleep(0.5)
    set_servo_angle(8, 90)
    set_servo_angle(9, 180)
    set_servo_angle(2, 90)
    set_servo_angle(3, 0)
    time.sleep(0.5)
    set_servo_angle(8, 45)
    set_servo_angle(9, 0)
    set_servo_angle(2, 180-45)
    set_servo_angle(3, 180)
    time.sleep(2)
    shutdown_all_servos()
    GPIO.cleanup()
