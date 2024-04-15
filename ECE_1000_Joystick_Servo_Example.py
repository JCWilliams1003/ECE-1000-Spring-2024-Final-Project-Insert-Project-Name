# This is an example code for using a joystick (X direction and Switch) with the ECE 1000 Raspberry Pi Pico Kit
# For any questions regarding this script, please email: jawilliams46@tntech.edu
# This script was inspired by the following source (YouTube video linked in website!): https://toptechboy.com/calibrating-joystick-to-show-positional-angle-in-micropython-on-the-raspberry-pi-pico-w/

# For this script, we utilize the Raspberry Pi Pico Kit that you are given along with the joystick from the sensors kit ... the joystick should be connected as follows:
# V_cc to the 3.3 Volt pin on the Pico Breadboard ... PLEASE USE 3.3 VOLT! 5 Volt will give incorrect values!
# GND to the GND pin on the Pico Breadboard
# VRx to the GPIO 26 pin on the Pico Breadboard (This is one of the ADC pins)
# SW to any GPIO pin ... let's say GPIO 16
# Using this code, try and figure out how you would connect the y-direction of the joystick

# The joystick utilizies two potentiometers and will output a voltage between two values depending on the position of the joystick (think of our Lab 1 session ... what happened when the potentiometer changed its resistance?)
# In order to read these ANALOG values (think real world, continuous values like temperature!), we must use an Analog to Digital Converter (ADC), which takes these continuous values and represents as signals the computer can understand (0, 1, etc...)

# How does this code work? Well, first we declare our libraries, then we delare what is hooked up to the Raspberry Pi Pico and to which pins they are connected, and finally we then ask the Pi Pico to show us the values of the joystick (FOREVER) .... (while True:)
from machine import PWM, ADC, Pin
import math
import utime

# What pins are hooked up to the joystick?
# This is saying that we have connected the x_direction of the joystick to the GPIO 26 pin (which is one of the ADC pins!)
adc_x_joystick = ADC(Pin(26))
# This is saying that we have conencted the switch pin of the joystick ... we are setting the Pin.PULL_UP meaning that the switch is normally at a 1 and then when pressed goes to 0 ... can also set this up reversed)
sw_joystick = Pin(16, Pin.IN, Pin.PULL_UP)
# This is saying that we are initializing the Pulse Width Modulation pins that will be used to control the position of the servo motor (50 Hz is a standard frequency for the pulse used to control the servos)
servo_x = PWM(Pin(0), freq=50)
servo_switch = PWM(Pin(1), freq = 50)

# This function will map the ADC value for the joystick to a value between -100 and 100 for ease of viewing (creating a slope between two points (m) and then creating a line y = mx + b)
# joystick_position = value from ADC (VRx)
# joystick_min = Move the joystick and see what the value is all the way left
# joystick_max = Move the joystick and see what the value is all the way right
# desired_min = -100 or 100 (depending on which direction of the joystick you want to be top or bottom)
# desired_max = 100 or -100 (^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^)
def get_joystick_value(joystick_position, joystick_min, joystick_max, desired_min, desired_max):
    m = ((desired_min - desired_max)/(joystick_min - joystick_max))
    return int((m*joystick_position) - (m*joystick_max) + desired_max)

# This function will take the value from the joystick (between -100 and 100) and then convert it to a duty cycle to be used to control the servo motor (for my servos: 0.5 ms = 0 degrees,  2.5 ms = 180 degrees, and the period of the wave is normally 20 ms [1/freq = 1/50 = 0.02 sec])
def get_servo_duty_cycle(joystick_value, min_angle_ms, max_angle_ms, period_ms, desired_min, desired_max):
    point_1_x = desired_min
    point_1_y = (min_angle_ms/period_ms)*65536
    point_2_x = desired_max
    point_2_y = (max_angle_ms/period_ms)*65535
    m = (point_2_y - point_1_y) / (point_2_x - point_1_x)
    return int((m*joystick_value) - (m*desired_min) + point_1_y)
    
# In this while loop, we will continually read the status (position) of the x direction and switch ... the value shown for x will be between 0 and 65535 ... as the 65535 is the maximum number that can be represented with an unsigned 16 bit integer
# however, we will be representing this number in terms of -100 to 100 in order to read the value more clearly ... so, -100 will represent the servo -90 degrees and 100 will represent the servo +90 degrees
while True:
    # What does the u_16 mean? This means unsigned integrer with 16 bits ... this is the RESOLUTION of our Analog to Digital Converter that is used to fully show where the joystick is!
    x_position = adc_x_joystick.read_u16() 
    # We don't need u16 here as value() will give us either 0 or 1 ... 1 will represent no push on the button and 0 will represent pushed down
    sw_status = sw_joystick.value()        
    
    # This portion will take the x value from the joystick and instead of showing them from 0 to 65535, will show them from -100 to 100 for ease of viewing. To do this, and to remove noise, we draw a line from -100 to 100 (y = mx+b) to get a linear change (see function above)
    x_value = get_joystick_value(x_position, 416, 65535, -100, 100)
    
    # This portion will find the maximum length of values (from -100 to 100) and then if we are close to 0 (meaning the joystick is in the middle), the values will be set to 0 to remove any jittering or noise
    range_of_values=math.sqrt(x_value**2)
    # Increase or decrease from 8 to get the joystick to read 0 at the middle position
    if range_of_values<=8:
        x_value=0
        
    # This portion will call the function above to get the joystick value into a useable form (duty cycle percentage)
    x_duty = get_servo_duty_cycle(x_value, 0.5, 2.5, 20, -100, 100)
    
    # This portion will get the value from the switch and will set it to the max value if the switch is pressed in (think of the claw opening if the switch is pressed) ... for this we just need to use the maximum angle for the servo (180) but represented in terms of ms (2.5 ms for my servo) and the period of the wave is 20 ms
    if sw_status == 0:
        sw_duty = int((2.5*65535)/20)
    else:
        sw_duty = int((0.5*65535)/20)
    
    # Now, update the servo motors
    servo_x.duty_u16(x_duty)
    servo_switch.duty_u16(sw_duty)
    
    # Finally, we print out the values so we can check what is happening as the code runs
    print(f"x_value is: {x_value},  x_duty is: {x_duty}, sw_status is: {sw_status}, sw_duty is: {sw_duty}")
    
    utime.sleep(0.1)