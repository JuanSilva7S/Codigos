import machine
import time

led_pins = [13,12,14,27,26,25,33,32,22]

leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

try:
    while True:
        print("Encendiendo todos los LEDs")
        for led in leds:
            led.on()  
        time.sleep(1)  

        print("Apagando todos los LEDs")
        for led in leds:
            led.off()  
        time.sleep(1)  

except KeyboardInterrupt:
    for led in leds:
        led.off()  
