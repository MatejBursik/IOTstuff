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
    wiringpi.pinMode(pinSwitch, 1) #write
    wiringpi.digitalWrite(pinLed, 0) #write 0 (low) to LED
    time.sleep(0.1)

    wiringpi.pinMode(pinSwitch, 0) #read
    time_measurement = [time.time(), 0]
    while wiringpi.digitalRead(pinSwitch) == 0:
        pass
    time_measurement[1] = time.time()
    print("Final time = ", time_measurement[1] - time_measurement[0])
