#!/bin/bash
while true 
do


gpio -g write 11 1

gpio -g write 11 0

done 
gpio -g write 11 1
