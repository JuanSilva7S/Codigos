import machine
import time

led_pins = [13,12,14,27,26,25,33,32,22]

leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

try:
    while True:
        for i, led in enumerate(leds):
            print(f"Encendiendo LED en pin {led_pins[i]}")
            led.on()
            time.sleep(0.5)
            led.off()
            time.sleep(0.5)

except KeyboardInterrupt:
    for led in leds:
        led.off()