import time, wiringpi, sys

#setup
print("Start")
pinLed = 2
pinSwitch = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinLed, 1)
wiringpi.pinMode(pinSwitch, 0)

#infinite loop - stop using Ctrl-C
while True:
    if wiringpi.digitalRead(pinSwitch) == 0: #input is active low
        print("Button Pressed")
        time.sleep(0.3) #anti bouncing
        wiringpi.digitalWrite(pinLed, 1) #write 1 (high) to LED
    else:
        print("Button released")
        time.sleep(0.3) #anti bouncing
        wiringpi.digitalWrite(pinLed, 0) #write 0 (low) to LED