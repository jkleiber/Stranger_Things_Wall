#include <Adafruit_NeoPixel.h>
#include <avr/power.h>

/*
enum CHAR_LEDS {
  LR = 1, LS, LT, LU, LV, LW, LX, LY, LZ, NAN1, LQ,
  LP, LO, LN, LM, LL, LK, LJ, LI, NAN2, LA, LB, LC,
  LD, LE, LF, LG, LH
};
*/

//Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel RZ = Adafruit_NeoPixel(9, 8, NEO_RGB + NEO_KHZ400);
Adafruit_NeoPixel AH = Adafruit_NeoPixel(8, 6, NEO_RGB + NEO_KHZ400);
Adafruit_NeoPixel QI = Adafruit_NeoPixel(9, 4, NEO_RGB + NEO_KHZ400);

String decodeKey = "ABCDEFGHQPONMLKJIRSTUVWXYZ";

String messages[10] = {
  "RUN AWAY",
  "STRANGER THINGS",
  "LOOK BEHIND YOU",
  "HASHTAG US",
  "HELP ME",
  "I HAVE BARB",
  "ITS WILL",
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
  "ZYXWVUTSRQPONMLKJIHGFEDCBA",
  "ABCDEFGHQPONMLKJIRSTUVWXYZ"
};
String message = String("HASHTAG US");

int normalDelayVal = 1000; // delay for a second

void setup() 
{
  Serial.begin(115200);
  //pixels.begin(); 
  AH.begin();
  QI.begin();
  RZ.begin();

  AH.show();
  QI.show();
  RZ.show();
}

void loop()
{
 
	if (Serial.available() > 0)
	{
		char inchar = Serial.read();
		
		String str = String(inchar);
		
		int index = decodeKey.indexOf(str);
		
		lightUp(index, normalDelayVal);
	}
	else
	{
		for(int ii = 0; ii < message.length(); ++ii)
		{
			int index = decodeKey.indexOf(message[ii]);
			
			lightUp(index, normalDelayVal);
		}
	}
	
	delay(1500);
  
}

//void lightUp(CHAR_LEDS charIndex)
void lightUp(int charIndex, int delayVal)
{
  if(charIndex < 8)
  {
    AH.setPixelColor(charIndex, AH.Color(255,255,255));
    AH.show();
    delay(delayVal);
    AH.setPixelColor(charIndex, AH.Color(0,0,0));
    AH.show();
    delay(delayVal);
  }
  else if(charIndex >= 8 && charIndex < 17)
  {
    QI.setPixelColor(charIndex-8, QI.Color(255,255,255));
    QI.show();
    delay(delayVal);
    QI.setPixelColor(charIndex-8, QI.Color(0,0,0));
    QI.show();
    delay(delayVal);
  }
  else
  {
    RZ.setPixelColor(charIndex-17, RZ.Color(255,255,255));
    RZ.show();
    delay(delayVal);
    RZ.setPixelColor(charIndex-17, RZ.Color(0,0,0));
    RZ.show();
    delay(delayVal);
  }
  
}

