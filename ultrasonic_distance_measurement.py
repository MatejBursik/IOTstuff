import time, wiringpi, sys

#setup
print("Start")
pinIn = 2
pinOut = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinIn, 0)
wiringpi.pinMode(pinOut, 1)

#infinite loop - stop using Ctrl-C
while True:
    wiringpi.digitalWrite(pinOut, 1)
    time.sleep(0.000001)
    wiringpi.digitalWrite(pinOut, 0)
    
    while wiringpi.digitalRead(pinIn) == 0:
        pass
    time_measurement = [time.time(), 0]
    while wiringpi.digitalRead(pinIn) == 1:
        pass
    time_measurement[1] = time.time()

    time_passed = time_measurement[1] - time_measurement[0]
    print("Distance =", time_passed * 17000)
    time.sleep(0.25)
