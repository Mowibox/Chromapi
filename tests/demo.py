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
            time.sleep(0.01) 

        for angle in range(ANGLE_MAX, ANGLE_MIN, -1):
            for channel in range(NUM_OF_CHANNELS):
                set_servo_angle(channel, angle)
            time.sleep(0.01) 

def servo_shutdown(channel):
    kit.servo[channel].set_pulse_width_range(0, 0)

def shutdown_all_servos():
    for channel in range(NUM_OF_CHANNELS):
        servo_shutdown(channel)
    
if __name__ == "__main__":
    move_all_servos()
    shutdown_all_servos()
    time.sleep(1)
    for i in range(5):
        GPIO.output(GPIO_LED_L, GPIO.LOW)
        GPIO.output(GPIO_LED_R, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(GPIO_LED_L, GPIO.LOW)
        GPIO.output(GPIO_LED_R, GPIO.LOW)
        time.sleep(0.2)

    GPIO.cleanup()
