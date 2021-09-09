#include <wiringPi.h>


int main(void)
{
wiringPiSetup(); /* initialize wiringPi setup */
pinMode(14, OUTPUT); /* set GPIO as output */

while (TRUE){
digitalWrite(14, HIGH); /* write high on GPIO */

digitalWrite(14, LOW); /* write low on GPIO */

}
return 0;
}
