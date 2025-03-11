# main.py -- put your code here!
from machine import ADC
from time import sleep
sleep()
potenciometro = ADC(Pin(25))
potenciometro.atten=(ADC.ATTN_11DB) #Siempre para evitar que se queme el microcontrolador

while True:
    valor=potenciometro.read()
    print(valor)
    sleep(1)
    

