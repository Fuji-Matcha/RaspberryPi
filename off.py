# -*- coding:utf-8 -*-
# すべてのGPIOピン27個をIN状態にする

import wiringpi as pi

def off():
    '''
    TURN OFF GPIO PINs

    '''
    gpios = [i+1 for i in range(27)]
    
    pi.wiringPiSetupGpio()

    for gpio in gpios :

        pi.pinMode(gpio, pi.OUTPUT)
        pi.digitalWrite(gpio, pi.LOW)
        pi.pinMode(gpio, pi.INPUT) 


if __name__ == '__main__':

    off()
