
# Inspired by https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/morse_code/
# Instead of working with a Raspberry Pi and and a LED, let's do it with a BlinkStick

import sys
import time
from blinkstick import blinkstick

def dot(bstick):
        bstick.set_color(red=0, green=255, blue=0)
        time.sleep(0.2)
        bstick.set_color(red=0, green=0, blue=0)
        time.sleep(0.2)
        return

def dash(bstick):
        bstick.set_color(red=0, green=255, blue=0)
        time.sleep(0.5)
        bstick.set_color(red=0, green=0, blue=0)
        time.sleep(0.2)
        return

CODE = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-'}

sticks = blinkstick.find_all()
if len(sticks) == 0:
        print "No blinkstick found."
        sys.exit()

# We work with the first blinkstick
bstick = sticks[0]

words = iter(sys.argv)
next(words)
for word in words:
        for letter in str(word):
                sys.stdout.write(letter)
                sys.stdout.write(': ')
                for symbol in CODE[letter.upper()]:
                        if symbol == "-":
                                dash(bstick)
                        elif symbol == ".":
                                dot(bstick)
                        else:
                                time.sleep(0.5)
                        sys.stdout.write(symbol)
                print 


bstick.turn_off()




