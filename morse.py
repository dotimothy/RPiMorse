#author Timothy Do
#RPiMorse Console: Prints Input in Morse Code to Console

#Libraries
import time


# Main Function, Prompt of Program
feed = ""
def main():
    print("Welcome to RPiMorse Console Version! It will convert your input into Morse Code and print to console.")
    feed = input("Type what you want to convert and press enter: ")
    print("Your input is " + feed + ".") 
    time.sleep(1)
    print("Here is your input in Morse Code!")
    time.sleep(1)
    printMorse(feed)

def printMorse(feed):
    for character in feed:
        print(character)

main()

