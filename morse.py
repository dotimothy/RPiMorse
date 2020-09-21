#author Timothy Do
#RPiMorse Console: Prints Input in Morse Code to Console

import time

#Functions for Dots, Dashes, and Slashes
def dot():
    print(".", end="")
    
def dash():
    print("-", end="")

def slash():
    print("/", end="")

#Functions for Printing the Letters
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

def k():
    dash()
    dot()
    dash()

def l():
    dot()
    dash()
    dot()
    dot()

def m():
    for i in range(0,2):
        dash()

def n():
    dash()
    dot()

def o():
    for i in range(0,3):
        dash()

def p():
    dot()
    dash()
    dash()
    dot()

def q():
    dash()
    dash()
    dot()
    dash()

def r():
    dot()
    dash()
    dot()

def s():
    for i in range(0,3):
        dot()
    
def t():
    dash()

def u():
    dot()
    dot()
    dash()

def v():
    for i in range(0,3):
        dot()
    dash()

def w():
    dot()
    dash()
    dash()

def x():
    dash()
    dot()
    dot()
    dash()

def y():
    dash()
    dot()
    dash()
    dash()

def z():
    dash()
    dash()
    dot()
    dot()

#Functions for Printing the Numbers
def one():
    dot()
    for i in range(0,4):
        dash()

def two():
    dot()
    dot()
    for i in range(0,3):
        dash()

def three():
    for i in range(0,3):
        dot()
    dash()
    dash()

def four():
    for i in range(0,4):
        dot()
    dash()

def five():
    for i in range(0,5):
        dot()

def six():
    dash()
    for i in range(0,4):
        dot()

def seven():
    dash()
    dash()
    for i in range(0,3):
        dot()

def eight():
    for i in range(0,3):
        dash()
    dot()
    dot()

def nine():
    for i in range(0,4):
        dash()
    dot()

def zero():
    for i in range(0,5):
        dash()

#Function to print the space
def space():
    slash()



#Function to traverese through input and printing to Morse Code.
def printMorse(input):
    for characters in input:
        nonMorse = characters != "a" and characters != "b" and characters != "c" and characters != "d" and characters != "e" and characters != "f" and characters != "g" and characters != "h" and characters != "i" and characters != "j" and characters != "l" and characters != "m" and characters != "n" and characters != "o" and characters != "p" and characters != "q" and characters != "r" and characters != "s" and characters != "t" and characters != "u" and characters != "v" and characters != "w" and characters != "x" and characters != "y" and characters != "z" and characters != "1" and characters != "2" and characters != "3" and characters != "4" and characters != "5" and characters != "6" and characters != "7" and characters != "8" and characters != "9" and characters != "0" and characters != ""
        if(characters == "a"):
            a()
        elif(characters == "b"):
            b()
        elif(characters == "c"):
            c()
        elif(characters == "d"):
            d()
        elif(characters == "e"):
            e()
        elif(characters == "f"):
            f()
        elif(characters == "g"):
            g()
        elif(characters == "h"):
            h()
        elif(characters == "i"):
            i()
        elif(characters == "j"):
            j()
        elif(characters == "k"):
            k()
        elif(characters == "l"):
            l()
        elif(characters == "m"):
            m()
        elif(characters == "n"):
            n()
        elif(characters == "o"):
            o()
        elif(characters == "p"):
            p()
        elif(characters == "q"):
            q()
        elif(characters == "r"):
            r()
        elif(characters == "s"):
            s()
        elif(characters == "t"):
            t()
        elif(characters == "u"):
            u()
        elif(characters == "v"):
            v()
        elif(characters == "w"):
            w()
        elif(characters == "x"):
            x()
        elif(characters == "y"):
            y()
        elif(characters == "z"):
            z()
        elif(characters == "1"):
            one()
        elif(characters == "2"):
            two()
        elif(characters == "3"):
            three()
        elif(characters == "4"):
            four()
        elif(characters == "5"):
            five()
        elif(characters == "6"):
            six()
        elif(characters == "7"):
            seven()
        elif(characters == "8"):
            eight()
        elif(characters == "9"):
            nine()
        elif(characters == "0"):
            zero()
        elif(characters == " "):
            space()
        elif(nonMorse):
            print("The Character \"" + characters + "\" Doesn't Exist in Morse. Please Try A Different Input.")
            prompt()
            exit()
        print(" ", end="")
    print()

#User Prompt
def prompt():
    feed = input("Type What You Want to Convert and Press Enter: ")
    if(feed == ""):
        print("You Didn't Input Anything. Please Try Again.")
        prompt()
    print("Your Input is " + feed + ".") 
    time.sleep(1)
    print("Here it is in Morse Code!")
    time.sleep(1)
    printMorse(feed.lower())



# Main Function, Welcomes You and Calls Prompt
def main():
    print("Welcome to RPiMorse Console Version! It will convert your input into Morse Code and print to console.")
    prompt()

        

main()

