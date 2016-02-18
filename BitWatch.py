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

def printtime():
    print(str(hours)+":"+str(minutes)+":"+str(seconds))

binaries = [one, two, three, four, five, six, seven, eight, nine, zero]

set = False


while True:
    sleep(500)
    fadesecs(3)
    sleep(500)
    fadesecs(6)
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
    elif mins > 9:
        minutes = [int(i) for i in str(mins)]
        binaries[minutes[0]-1](3)
        binaries[minutes[1]-1](4)
    if hrs<10:
        binaries[hrs-1](1)
        zero(0)
    elif hrs > 9:
        hours = [int(i) for i in str(hrs)]
        binaries[hours[0]-1](0)
        binaries[hours[1]-1](1)

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
