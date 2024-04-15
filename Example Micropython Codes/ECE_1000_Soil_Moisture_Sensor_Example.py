# This is an example code for using a Capacitive Soil Moisture probe with the ECE 1000 Raspberry Pi Pico Kit
# For any questions regarding this script, please email: jawilliams46@tntech.edu

# For this script, we utilize the Raspberry Pi Pico Kit that you are given along with the capacitive soil moisture probe which should be connected as follows:
# V_cc to the 3.3 Volt or 5 Volt pin on the Pico Breadboard
# GND to the GND pin on the Pico Breadboard
# AOUT to the GPIO 26 pin on the Pico Breadboard (This is one of the ADC pins)

# How does this code work? Well, first we declare our libraries, then we delare what is hooked up to the Raspberry Pi Pico and to which pins they are connected, and finally we then ask the Pi Pico to show us the values of the probe as a percentage (FOREVER) .... (while True:)
from machine import ADC, Pin
import utime

# What pins are hooked up to the joystick?
# This is saying that we have connected the data pin of the sensor to the GPIO 26 pin (which is one of the ADC pins!)
soil_probe = ADC(Pin(26))

# Before we can show the moisture as a percentage, need to first get the minimum moisture value (when the probe is not in water) and the maximum moisture value (when the probe is in water)
max_moisture = 27574
min_moisture = 57100

# This function will fit the moisture level of the sensor to a line equation from ~0% to ~100% using the min and max moisture value measured with the sensor 
def get_moisture_percentage(moisture_level):
    point_1_x = min_moisture
    point_2_x = max_moisture
    point_1_y = 0
    point_2_y = 100
    m = ((point_2_y - point_1_y) / (point_2_x - point_1_x))
    return int((m*moisture_level) - (m*min_moisture) + point_1_y)

# Now, forever (while True:), read the value from the moisture sensor, convert it to a percentage, and display in the shell for users to see
while True: 
    moisture_level = soil_probe.read_u16()
    
    # This will fit the data from the soil moisture probe to a line equation between ~0% moisture and ~100% moisture
    moisture_level_percentage = get_moisture_percentage(moisture_level)
    
    print(moisture_level_percentage)
    
    utime.sleep(0.8)