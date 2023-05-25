#define period 5  //define period of measurement in sec. defult is 5 sec.
#define RED 0     //define red color pin
#define GREEN 2   //define green color pin
#define BLUE 3    //define blue color pin

#include <DHT.h>    //dht sensor library
DHT dht(4, DHT11);  //sensor pin=4, dht type=dht11

void setup()
{
  pinMode (RED,OUTPUT);  
  pinMode (GREEN,OUTPUT);  
  pinMode (BLUE,OUTPUT); 
  dht.begin();
}

void loop()
{ float t = dht.readTemperature();
  float h = dht.readHumidity();


  if (isnan(t) ) {          //temperature sensor check. if error->fast blink buildin led
  digitalWrite(RED, LOW);  
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE, LOW);
  digitalWrite(1, HIGH);    //default buildin led=1 for Digispark USB
  delay(250); 
  digitalWrite(1, LOW);
  return;
  }

for (int i=0; i <= 3; i++){   //humidity check for optimum 15%-40%
  if (h >= 40 || h <= 15){
    {digitalWrite (RED, HIGH);
     digitalWrite (GREEN, LOW);
     digitalWrite (BLUE, LOW);
     delay(250);  
     digitalWrite (RED, LOW);
     digitalWrite (GREEN, HIGH);
     digitalWrite (BLUE, LOW);
     delay(250);
     digitalWrite (RED, LOW);
     digitalWrite (GREEN, LOW);
     digitalWrite(BLUE, HIGH);
     delay(250);}
    }}  
  
  if (t >25)  //temperature check for hot, cold, optimum
    {digitalWrite (RED, HIGH);
     digitalWrite (GREEN, LOW);
     digitalWrite (BLUE, LOW);}
    
  else if (t <23)
    {digitalWrite (RED, LOW);
     digitalWrite (GREEN, LOW);
     digitalWrite (BLUE, HIGH);}
    
  else
    {digitalWrite (RED, LOW);
     digitalWrite (GREEN, HIGH);
     digitalWrite (BLUE, LOW);}

  delay(period*1000);   //period of measurement delay
}
