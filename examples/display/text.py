##
# This example shows some text on the display
# Based on the examples provided by the Adafruit library
#

import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# reset pin
RST = None
# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
# Initialize library.
disp.begin()
# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.heightcd
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()

draw.rectangle((0,0,width,height), outline=0, fill=0)

# Write two lines of text.

draw.text((x, top),       "test",  font=font, fill=255)
draw.text((x, top+8),     "Hello you", font=font, fill=255)
draw.text((x, top+16),    "I'm alive?",  font=font, fill=255)
draw.text((x, top+25),    "______________________",  font=font, fill=255)

# Display image.
disp.image(image)
disp.display()
