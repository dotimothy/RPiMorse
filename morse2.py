#author Timothy Do
#RPiMorse Console: Prints Input in Morse Code to Console
#Note: Only works with Python2 (No Spanish Characters), For Python3, run morse.py

import time

#Functions for Dots, Dashes
def dot():
    print("."),
    
def dash():
    print("-"),
    
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
    
#Function to Print Punctuation
def period():
    for i in range(0,3):
        dot()
        dash()

def comma():
    dash()
    dash()
    dot()
    dot()
    dash()
    dash()

def question():
    dot()
    dot()
    dash()
    dash()
    dot()
    dot()

def apostrophe():
    dot()
    for i in range(0,4):
        dash()
    dot()


def exclamation():
    for i in range(0,2):
        dash()
        dot()
    dash()
    dash()

def slash():
    dash()
    dot()
    dot()
    dash()
    dot()


def leftBracket():
    dash()
    dot()
    dash()
    dash()
    dot()

def rightBracket():
    dash()
    dot()
    dash()
    dash()
    dot()
    dash()


def ampersand():
    dot()
    dash()
    for i in range(0,3):
        dot()

def colon():
    for i in range(0,3):
        dash()
    for j in range(0,3):
        dot()

def semicolon():
    for i in range(0,3):
        dash()
        dot()
        
#Fucntions to print arithmetic signs
def equal():
    dash()
    for i in range(0,3):
        dot()
    dash()

def plus():
    for i in range(0,2):
        dot()
        dash()
    dot()

def minus():
    dash()
    for i in range(0,4):
        dot()
    dash()

#Functions to print some shift characters
def underscore():
    dot()
    dot()
    dash()
    dash()
    dot()
    dash()


def doubleQuote():
    dot()
    dash()
    dot()
    dot()
    dash()
    dot()


def dollarSign():
    for i in range(0,3):
        dot()
    dash()
    dot()
    dot()
    dash()


def atSign():
    dot()
    dash()
    dash()
    dot()
    dash()
    dot()
    
#Function to print the space
def space():
    print("/"),

#Function to traverese through input and printing to Morse Code.
def printMorse(input):
    #For Checking for Invalid Characters
    for character in input.lower():
        nonMorse = character != "a" and character != "b" and character != "c" and character != "d" and character != "e" and character != "f" and character != "g" and character != "h" and character != "i" and character != "j" and character != "k" and character != "l" and character != "m" and character != "n" and character != "o" and character != "p" and character != "q" and character != "r" and character != "s" and character != "t" and character != "u" and character != "v" and character != "w" and character != "x" and character != "y" and character != "z" and character != "1" and character != "2" and character != "3" and character != "4" and character != "5" and character != "6" and character != "7" and character != "8" and character != "9" and character != "0" and character != "." and character != "," and character != "?" and character != "'" and character != "!" and character !="/" and character != "(" and character != ")" and character != "&" and character != ":" and character != ";" and character != "=" and character != "+" and character != "-" and character != "_" and character != "\"" and character != "$" and character != "@" and character != " " and character != ""
        if(nonMorse):
            print("The Character \'" + character + "\' in Input \"" + input + "\" Doesn't Exist in Morse Code. Please Try A Different Input.")
            prompt()
            exit()
    #For Printing
    for characters in input.lower():
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
        elif(characters == "."):
            period()
        elif(characters == ","):
            comma()
        elif(characters == "?"):
            question()
        elif(characters == "'"):
            apostrophe()
        elif(characters == "!"):
            exclamation()
        elif(characters == "("):
            leftBracket()
        elif(characters == ")"):
            rightBracket()
        elif(characters == "&"):
            ampersand()
        elif(characters == "/"):
            slash()
        elif(characters == ":"):
            colon()
        elif(characters == ";"):
            semicolon()
        elif(characters == "="):
            equal()
        elif(characters == "+"):
            plus()
        elif(characters == "-"):
            minus()
        elif(characters == "_"):
            underscore()
        elif(characters == "\""):
            doubleQuote()
        elif(characters == "$"):
            dollarSign()
        elif(characters == "@"):
            atSign()
        elif(characters == " "):
            space()
        print(" "),
    print("\n\nThe output has been compiled.\n")
    exit()

#User Prompt
def prompt():
    feed = raw_input("\nType What You Want to Convert and Press Enter: ")
    if(feed == ""):
        print("You Didn't Input Anything. Please Try Again.")
        prompt()
    print("\nYour Input is " + feed + ".\n")   
    print("Here it is in Morse Code!")
    printMorse(feed)
    
# Main Function, Welcomes You and Calls Prompt
def mainTwo():
    print("Welcome to RPiMorse for Python2! It will convert your input into Morse Code and print to console.")
    print("Note: morse2.py cannot convert spanish characters. Please use the main program morse.py and Python3.")
    prompt()


