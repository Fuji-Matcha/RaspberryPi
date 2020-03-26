import wiringpi as pi

def onoff():

    LED = 14
    
    pi.wiringPiSetupGpio()
    pi.pinMode(LED, pi.OUTPUT)
    pi.softPwmCreate( LED, 0, 100)

    for k in range(10):
        
        for i in range(100):

            pi.softPwmWrite( LED, i)
            pi.delay(5)
    
        for j in range(100):

            pi.softPwmWrite( LED, 99-j)
            pi.delay(5)

    pi.digitalWrite( LED, pi.HIGH )
    pi.digitalWrite( LED, pi.LOW )
    


if __name__ == '__main__' :

    onoff()
