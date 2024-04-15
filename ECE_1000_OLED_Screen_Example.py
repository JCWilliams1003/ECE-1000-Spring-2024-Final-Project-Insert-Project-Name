# This is an example code for using an OLED screen with the ECE 1000 Raspberry Pi Pico Kit
# For any questions regarding this script, please email: jawilliams46@tntech.edu

# Step 1: Download the ssd1306.py script, save it onto the Raspberry Pi Pico WH (Very Important!)

# Step 2: Import the needed package/libraries
# machine: Allows us to manipulate the Pins and Protocols of the R Pi Pico WH
# ssd1306: Allows us to use OLED library "ssd1306.py" to control the OLED screen
# time: Allows us to execute actions at a specific time based off the R Pi Pico clock

# import the machine library and allow for us to use the Pin and I2C commands easily (I2C is a communication protocol that we will use to communicate between the R Pi Pico and the OLED screen
from machine import Pin, I2C
import ssd1306
import time

# Initialize the I2C communication protocol to use with the R Pi Pico ... we MUST connect the SCL pin to GPIO 4 and the SDA to GPIO 5 ... these are DEDICATED pins on the R Pi Pico WH
# 400,000 Hz is the communication frequency for the I2C protocol
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# Initialize the OLED Display (Declare the Screen Width and Height in pixels ... so we can make sure the message is displayed correctly and in a readable way on the screen)
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Clear the display and get it ready for it's first use
oled.fill(0)
oled.show()

# Display the message that you want users to be able to read (the first digit is the x position and the second digit is the y position ... these are the locations (in pixels) where the text is displayed)
# For this OLED ... anything from height 0 to 16 will be yellow text, otherwise the text will be blue
oled.text('Hello World!', 0, 0)
oled.text('ECE 1000 S24', 0, 20)
# With this you will see that the text is too long and the last half goes off the screen ... need to take this into consideration! If it goes off the screen, just make multiple messages!
oled.text('What is better, Ralphs or Big-Os?', 0, 40)
oled.show()

# Now, need some buffer time for the screen to wait between displaying the next messages ... has to be on the screen lon enough for us to read!
time.sleep(2)

# We can also use the library we imported to display simple shapes and patterns ...
oled.fill(0)
# Don't forget, the y location of the pixels might change the color! 0 to 16 are yellow ... else blue
# The oled.rect(x, y, w, h, color) method draws a rectangle on the OLED screen with its top-left corner at (x, y), width w, height h, and use a color that will show up (1 = color, 0 = black screen)
oled.rect(10, 10, 50, 20, 1)
#The oled.fill_rect(x, y, w, h, color) method draws a filled rectangle on the OLED screen with its top-left corner at (x, y), width w, height h, and filled with color color (1 = color,, 0 = black screen)
oled.fill_rect(70, 10, 50, 20, 1)
# Now, show what you specified onto the screen ...
oled.show()
time.sleep(2)

# Now, an example from the library's website to draw the Micropython Logo: https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html
oled.fill(0)
oled.fill_rect(0, 17, 32, 32, 1)
oled.fill_rect(2, 19, 28, 28, 0)
oled.vline(9, 25, 22, 1)
oled.vline(16, 19, 22, 1)
oled.vline(23, 25, 22, 1)
oled.fill_rect(26, 41, 2, 4, 1)
oled.text('MicroPython', 40, 17, 1)
oled.text('SSD1306', 40, 29, 1)
oled.text('OLED 128x64', 40, 41, 1)
oled.show()

time.sleep(2)

# Thanks! Again, remember, if you have any questions just:
oled.fill(0)
oled.text('Email JC!:', 0, 0)
oled.text('jawilliams46', 0, 20)
oled.text('@tntech.edu', 0, 30)
oled.text('Thanks!', 0, 50)
oled.show()