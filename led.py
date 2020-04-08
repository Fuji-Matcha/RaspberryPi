import wiringpi as pi

def main():

    LED_PIN = 7
    pi.wiringPiSetupGpio()
    pi.pinMode( LED_PIN, pi.OUTPUT )
    pi.digitalWrite( LED_PIN, pi.HIGH)
    pi.delay(5000)
    pi.digitalWrite( LED_PIN, pi.LOW)

if __name__ == "__main__" :

    main()


