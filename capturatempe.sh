#!/bin/bash

#El script captura la informacion del sensor
 #transforma el valor de tempertura
#y guarda los valores junto a la fecha cada 10 segundos.


echo "Ejecutando el script .... para finalizar presione Ctrl + c "

while true
do
a=$(date +%Y%m%d%H%M%S)
b=$(cat /sys/bus/w1/devices/28-00000ba3e3d8/temperature)


c=$(echo $((b/1000)).$((b%100))'°C')
echo $a';'$c >> $(date +%Y%m%d)_TEMPERATURA.csv
sleep 1
done
