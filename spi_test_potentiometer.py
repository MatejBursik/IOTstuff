import wiringpi
import time

def ActivateADC ():
    wiringpi.digitalWrite(pin_CS_adc, 0)       # Actived ADC using CS
    time.sleep(0.000005)

def DeactivateADC():
    wiringpi.digitalWrite(pin_CS_adc, 1)       # Deactived ADC using CS
    time.sleep(0.000005)

def readadc(adcnum): 
    if ((adcnum > 7) or (adcnum < 0)): 
        return -1 
    revlen, recvData = wiringpi.wiringPiSPIDataRW(1, bytes([1,(8+adcnum)<<4,0]))
    time.sleep(0.000005)
    adcout = ((recvData[1]&3) << 8) + recvData[2] 
    
    return adcout 

#Setup
pin_CS_adc = 16                                 #We will use w16 as CE, not the default pin w15!
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin_CS_adc, 1)                 # Set ce to mode 1 ( OUTPUT )
wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0)  #(channel, port, speed, mode)
#pin 5 and 7
wiringpi.pinMode(5, 1)
wiringpi.pinMode(7, 1)
wiringpi.digitalWrite(5, 0)
wiringpi.digitalWrite(7, 0)

#Main
try:
    while True:
        ActivateADC()
        tmp0 = readadc(0) # read channel 0
        DeactivateADC()
        print ("input0:",tmp0)
        time.sleep(0.2)

        ActivateADC()
        tmp1 = readadc(1) # read channel 1
        DeactivateADC()
        print ("input1:",tmp1)
        time.sleep(0.2)

        if tmp0 > tmp1:
            wiringpi.digitalWrite(5, 0)
            wiringpi.digitalWrite(7, 1)
        elif tmp1 > tmp0:
            wiringpi.digitalWrite(5, 1)
            wiringpi.digitalWrite(7, 0)
        elif tmp1 == tmp0:
            wiringpi.digitalWrite(5, 0)
            wiringpi.digitalWrite(7, 0)
    
except KeyboardInterrupt:
    DeactivateADC()
    print("\nProgram terminated")
    
