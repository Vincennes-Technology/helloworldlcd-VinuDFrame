#!/usr/bin/python
#show "Hello World on the LCD screen"
# DFrame

import Adafruit_CharLCD as LCD
import time

lcd = LCD.Adafruit_CharLCDPlate()

displayText = "Hello World\n"

lcd.clear()
lcd.message(displayText)

while (True):
    if lcd.is_pressed(LCD.UP):
        lcd.set_backlight(1)
        lcd.message(displayText)

    else:
        lcd.set_backlight(0)
        lcd.clear()
        time.sleep(0.5)
