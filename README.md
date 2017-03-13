Stranger Things Wall project
============================

Send your own messages from the upside down with this creepy project!

Using individually addressable LEDs, I have adapted Sparkfun's original code that
recreated Joyce's Christmas light message board from the Netflix original
series "Stranger Things". In this repository, you'll find the code necessary to
enable a string of LEDs to capture and display tweets.

You'll need an Arduino to communicate with the LEDs (I used an Arduino Uno r3) and some kind of PC that
can run Python (I used a [pcDuino3](https://www.sparkfun.com/products/12856)
because of its built in WiFi and native Python support. However, any internet enabled SBC should work).

The Arduino code was written in the Arduino.cc IDE v1.8.1, and the Python code
is running under Python 2.7.3. You'll need the Adafruit Neopixel library, which
can be found in the Library Manager inside the Arduino IDE.

On the pcDuino, you will need to install the serial library which can be installed via pip.
Furthermore, you will need to ensure that the pcDuino has a good connection to the internet.

Additionally, you'll have to create your own "credentials.py" file with your
Twitter application credential details; see
[apps.twitter.com](apps.twitter.com) for more information on doing just that.
Make sure your credentials file uses the same variable names as the main python code.