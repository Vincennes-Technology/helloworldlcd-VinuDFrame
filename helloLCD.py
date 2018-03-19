#!/usr/bin/python
#show "Hello World on the LCD screen"
# DFrame

import Adafruit_CharLCD as LCD
import time
import subprocess

lcd = LCD.Adafruit_CharLCDPlate()

displayText = "Hello World"

Name = subprocess.check_output(['hostname']).strip()
IPaddr = subprocess.check_output(['hostname','-I'])
displayText2 = IPaddr + Name

lcd.clear()
lcd.set_backlight(1)
while (True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.message(displayText)
    else:
        lcd.clear()
        lcd.message(displayText2)
    #time.sleep(0.5)
