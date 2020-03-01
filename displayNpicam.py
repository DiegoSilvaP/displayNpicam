import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import time
import picamera

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

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
height = disp.height
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

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia2.ttf', 8)

try:
    with picamera.PiCamera() as picam:
    picam.start_preview()
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Write two lines of text.
    draw.text((x, top),       "Initializing cam...",  font=font, fill=255)
    time.sleep(5)
    picam.capture('nombre.jpg')
    draw.text((x, top+8),     "nombre.jpg captured", font=font, fill=255)
    picam.stop_preview()
    draw.text((x, top+16),    "Stopping camera",  font=font, fill=255)
    picam.close()
    draw.text((x, top+25),    "Success :)",  font=font, fill=255)
except expression as identifier:
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Write two lines of text.
    draw.text((x, top),       "Error with camera",  font=font, fill=255)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Write two lines of text.
draw.text((x, top),       "Hola mundo...",  font=font, fill=255)
draw.text((x, top+8),     "Testeando display", font=font, fill=255)
draw.text((x, top+16),    "Aquí va el txt de ASL",  font=font, fill=255)
draw.text((x, top+25),    "vamos a probar la picam",  font=font, fill=255)

# Display image.
disp.image(image)
disp.display()