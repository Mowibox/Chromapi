"""
    @file        test_2.py
    @author      Mowibox (Ousmane THIONGANE)
    @brief       Ultrasonic sensor test to check Chromapi functionalities
    @version     1.0
    @date        2024-10-26
    
"""

# Includes 
import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit

GPIO_LED_L = 23    
GPIO_LED_R = 22 

GPIO_TRIG = 4
GPIO_ECHO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_LED_L, GPIO.OUT)  
GPIO.setup(GPIO_LED_R, GPIO.OUT) 
GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_LED_L, GPIO.LOW)
GPIO.output(GPIO_LED_R, GPIO.LOW)

NUM_OF_CHANNELS = 16
DISTANCE_THRESHOLD = 10

val = 0
still_goal = False

kit = ServoKit(channels=NUM_OF_CHANNELS)


def set_servo_angle(channel: int, angle: float):
    """
    Sets the servomotor to the target angle

    @param channel: The channel number
    @param angle: The angle in degrees
    """
    if 0 <= channel < 16 and 0 <= angle <= 180:
        kit.servo[channel].angle = angle
    else:
        print("Invalid value for channel or angle! channel must be between [0-15] and angle between [0-180].")

def servo_shutdown(channel: int):
    """
    Turns off the servomotor on the specified channel

    @param channel: The channel number
    """
    kit.servo[channel].angle = None

def get_distance() -> float:
    """
    Returns the distance measured by the ultrasonic sensor in cm
    """
    GPIO.output(GPIO_TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG, GPIO.LOW)

    start = time.time()
    while GPIO.input(GPIO_ECHO) == GPIO.LOW:
        start = time.time()
    
    stop =  time.time()
    while GPIO.input(GPIO_ECHO) == GPIO.HIGH:
        stop = time.time()

    delta_time = stop - start

    distance = (delta_time* 34300)/2

    return distance


try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance:.1f} cm")

        if distance < DISTANCE_THRESHOLD:
            still_goal = False
            GPIO.output(GPIO_LED_L, val)
            GPIO.output(GPIO_LED_R, 1-val)
            set_servo_angle(8, 90*(1-val))
            set_servo_angle(9, 90*(2-val))
            val = (val+1)%2
        else:
            if not(still_goal):
                set_servo_angle(8, 45)
                set_servo_angle(9, 0)
                time.sleep(1.5)
                servo_shutdown(8)
                servo_shutdown(9)
                still_goal = True
            GPIO.output(GPIO_LED_L, GPIO.LOW)
            GPIO.output(GPIO_LED_R, GPIO.LOW)

        time.sleep(0.5)

except KeyboardInterrupt:
    set_servo_angle(8, 45)
    set_servo_angle(9, 0)
    time.sleep(1)
    servo_shutdown(8)
    servo_shutdown(9)
    GPIO.cleanup()

        



