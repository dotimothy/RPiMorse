# [RPiMorse](https://github.com/dotimothy/RPiMorse)
A python program to convert standard input to morse code, printing to console (all) or flashing an LED via GPIO Pins (Pin 11). Run <code>morse.py</code> to get a universal Morse Code translator on console for any device with Python,or run <code>rpi.py</code> if you have a Raspberry Pi with an LED circuit for more real world translations!

<img src="console.gif">
<img src="led.gif">
 
 ## Global Requirments:
 Python Version 2 or higher
 <br>
 ### For Pi Version:
 Raspberry Pi with GPIO Pins 
 <br>
 An LED
 <br>
 A 100 Ω Resistor
 <br>
 A Breadboard
 <br>
 3+ Jumper Wires (More for Stablity)
 
 ## Setup
 RPiMorse uses the following translations to convert regular input to Morse Code:
 <img src="morse.png">
 For the LED Version, construct the following circuit: 
 <img src="circuit.jpg">
 
  # Documentation for Pi Version:
 
 For testing purposes, if your python version is 3 or higher, please run the program <code>rpi3.py</code>. If your version is lower, run <code>rpi2.py</code>.
 
  ## Or just run <code>rpi.py</code> for guranteed console functionality (chooses version for you, even with no Pi!).
  
  <img src="rpi.PNG">
 
 # Documentation for Console Versions: 
 For testing purposes, if your python version is 3 or higher, please run the program <code>morse3.py</code>. If your version is lower, run <code>morse2.py</code>.
 
 ## Or just run <code>morse.py</code> for guranteed console functionality (chooses version for you!).
<img src="console.png">


