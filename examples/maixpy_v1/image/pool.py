#!/usr/bin/env python

from maix.v1 import lcd, image
from maix import time

lcd.init()

img = image.Image("test.jpg")
img.mean_pool(2, 2)
lcd.display(img)
time.sleep(1)

img = image.Image("test.jpg")
img.midpoint_pool(3, 3)
lcd.display(img)

while True:
    time.sleep(1)
