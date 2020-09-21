#author Timothy Do
#RPiMorse Console: Prints Input in Morse Code to Console

import time

def dot():
    print(".", end="")
    
def dash():
    print("-", end="")

def slash():
    print("/", end="")

def a():
    dot()
    dash()

def b():
    dash()
    for i in range(0,3):
        dot()

def c():
    dash()
    dot()
    dash()
    dot()

def d():
    dash()
    dot()
    dot()

def e():
    dot()

def f():
    dot()
    dot()
    dash()
    dot()

def g():
    dash()
    dash()
    dot()

def h():
    for i in range(0,4):
        dot()

def i():
    dot()
    dot()

def j():
    dot()
    for i in range(0,3):
        dash()

def printMorse(input):
    for characters in input:
        if(characters == "a"):
            a()
        if(characters == "b"):
            b()
        if(characters == "c"):
            c()
        if(characters == "d"):
            d()
        if(characters == "e"):
            e()
        if(characters == "f"):
            f()
        if(characters == "g"):
            g()
        if(characters == "h"):
            h()
        if(characters == "i"):
            i()
        if(characters == "j"):
            j()    

        print(" ", end="")



# Main Function, Prompt of Program
feed = ""
def main():
    print("Welcome to RPiMorse Console Version! It will convert your input into Morse Code and print to console.")
    feed = input("Type what you want to convert and press enter: ")
    print("Your input is " + feed + ".") 
    time.sleep(1)
    print("Here it is in Morse Code!")
    time.sleep(1)
    printMorse(feed.lower())
        

main()

