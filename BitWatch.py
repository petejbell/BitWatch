                                                                                                                                        '''
'BitWatch' is a Binary Watch programme written in MicroPython for the BBC Micro:bit by @petejbell and distributed under a MIT licence
Please share with me what you do with it, I'd love to see what you do!
You can find a tutorial showing you how to build a strap for your watch here: https://t.co/li9CktVJhg

Instructions:
1)  Download Mu from here: https://github.com/ntoll/mu
2)  Copy and paste this BitWatch code to Mu, connect your Micro:bit to your computer and then flash the code to your Micro:bit
3)  The BitWatch will display 23:59 as the time for 10 seconds and will then show 'midnight' (00:00).
    Use Button A to set the Hours and B to set the Minutes. Hold each one down and you will see the hours/minutes increment.
    Use Buttons A+B together to reset seconds to '0'.
    
        Column 0 shows the first digit in the hours (in 24hr clock) and column 1 shows the second digit.
        Column 3 shows the first digit in the minutes and column 4 shows the second digit.
        Column 2 shows the seconds flashing away.

For a crash course on binary, see here: http://www.bbc.co.uk/education/guides/z26rcdm/revision/1                                        '''

from microbit import *

sec = 50
seconds = []
mins = 59
minutes = []
hrs = 23
hours = []
b = 8 #brightness

def one(x):
    zero(x)
    display.set_pixel(x, 3, b),
        
def two(x):
    zero(x)
    display.set_pixel(x, 2, b),

def three(x):
    zero(x)
    display.set_pixel(x, 3, b)
    display.set_pixel(x, 2, b),
    
def four(x):
    zero(x)
    display.set_pixel(x, 1, b),

def five(x):
    zero(x)
    display.set_pixel(x, 3, b)
    display.set_pixel(x, 1, b),

def six(x):
    zero(x)
    display.set_pixel(x, 2, b)
    display.set_pixel(x, 1, b),

def seven(x):
    zero(x)
    display.set_pixel(x, 1, b)
    display.set_pixel(x, 2, b)
    display.set_pixel(x, 3, b),

def eight(x):
    zero(x)
    display.set_pixel(x, 0, b),

def nine(x):
    zero(x)
    display.set_pixel(x, 0, b)
    display.set_pixel(x, 3, b),
    
def zero(x):
    for i in range(0,4):
        display.set_pixel(x, i, 0)

def fadesecs(x):
    display.set_pixel(2, 2, x)
    display.set_pixel(2, 1, x)
    
def background(x,y):
    if display.get_pixel(x, y) < 1:
        display.set_pixel(x, y, 1)
        
def backgrounds():
    background(0,0)
    background(0,1)
    background(0,2)
    background(0,3)
    background(1,0)
    background(1,1)
    background(1,2)
    background(1,3)
    background(3,0)
    background(3,1)    
    background(3,2)    
    background(3,3)    
    background(4,0)
    background(4,1)
    background(4,2)
    background(4,3)
    
def printtime():
    print(str(hours)+":"+str(minutes)+":"+str(seconds))

binaries = [one, two, three, four, five, six, seven, eight, nine, zero]

set = False


while True:
    sleep(500)
    fadesecs(1)
    sleep(500)
    fadesecs(4)
    sec += 1
    if sec % 60 == 0:
        mins += 1
        sec = 0
        if mins % 60 == 0:
            hrs += 1
            mins = 0
            if hrs % 24 == 0:
                hrs = 0
    seconds=str(sec)
    minutes=str(mins)
    hours=str(hrs)
    printtime()

    
    if mins<10:
        binaries[mins-1](4)
        zero(3)
        backgrounds()
    elif mins > 9:
        minutes = [int(i) for i in str(mins)]
        binaries[minutes[0]-1](3)
        binaries[minutes[1]-1](4)
        backgrounds()
    if hrs<10:
        binaries[hrs-1](1)
        zero(0)
        backgrounds()
    elif hrs > 9:
        hours = [int(i) for i in str(hrs)]
        binaries[hours[0]-1](0)
        binaries[hours[1]-1](1)
        backgrounds()


    if button_a.is_pressed() and button_b.is_pressed():
        if sec < 60:
            sec = 1
        sleep(100)
    if button_a.is_pressed():
        if hrs < 24:
            hrs += 1
        else:
            hrs = 0
        sleep(100)
    if button_b.is_pressed():
        if mins < 60:
            mins += 1
        else:
            mins = 0
        sleep(100)
