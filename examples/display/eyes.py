#
# This example shows the image of the eyes on the display
# Based on the examples provided by the Adafruit library
#

import time
import Adafruit_SSD1306
from PIL import Image

# reset pin
RST = None

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

image = Image.open('eyes.ppm').convert('1')

# Display image.
disp.image(image)
disp.display()
