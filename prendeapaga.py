import time 
#!usr/bin/env/ python
#enciende.py
#importamos la libreria GPIO
import RPi.GPIO as GPIO 
#Definimos el modo BCM

GPIO.setmode(GPIO.BCM) 
#Ahora definimos el pin 11
GPIO.setup(11, GPIO.OUT) 
#Y le damos un valor logico alto para encender el LED

#ciclo
while (1):
#prendemosled
    GPIO.output(11, GPIO.HIGH)
#apagamosled
    GPIO.output(11, GPIO.LOW)


#liberamos todos los pines GPIO, es decir, los desconfiguramos)
GPIO.cleanup()



