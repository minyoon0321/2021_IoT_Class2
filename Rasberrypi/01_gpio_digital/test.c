#include <wiringPi.h>
#define LED_PIN 4
#define LED_PIN 5
#define LED_PIN 6

int main (void){
    wiringPiSetupGpio();
    pinMode (LED_PIN_1, OUTPUT);
    pinMode (LED_PIN_2, OUTPUT);
    pinMode (LED_PIN_3, OUTPUT);

    digitalwrite(LED_PIN_1, HIGH);
    delay (200);
    digitalwrite(LED_PIN_1, LOW);

    digitalwrite(LED_PIN_2, HIGH);
    delay (200);
    digitalwrite(LED_PIN_2, LOW);

    digitalwrite(LED_PIN_3, HIGH);
    delay (200);
    digitalwrite(LED_PIN_3, LOW);
    
    return 0;
}