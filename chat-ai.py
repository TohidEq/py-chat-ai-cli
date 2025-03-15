#!/usr/bin/env python

from os import system, name
from rich.console import Console
from rich.markdown import Markdown
import keyboard
import sys

MARKDOWN_MODE = True;

# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



"""
    >> Gets user multiple lines input and end inputs by pressing Ctrl + Enter
    1. Returns it as a string(with "\n" for going next line)
    2. Returns (False) if first input was empty
"""
def get_input():
    lines = []
    print(">> ",end="")
    while True:
        # Get input from the user
        line = input()

        # Check first line is empty
        if len(lines)==0: # is first line?
            if len(line)==0: # is input empty?
                return False

        # Add input to lines
        lines.append(line)

        # Check if Ctrl + Enter has been pressed
        if keyboard.is_pressed('ctrl+enter'):
            return "\n".join(lines)





def print_markdown(text):
    if MARKDOWN_MODE:
        Console().print(Markdown(text))
    else:
        print(text)

def print_borderized(text):
    print_markdown("---")
    print_markdown(text)
    print_markdown("---")



    #md = Markdown("result of chat here")
def main():
    global MARKDOWN_MODE
    # Check Args
    user_args= ' '.join(sys.argv[1:])
    if user_args in ["markdown=off","markdown=false","markdown=False","markdown=0"]:
        MARKDOWN_MODE = False


    clear()
    #console.print(md)
    app_alive = True
    print_markdown("---")
    if MARKDOWN_MODE:
        print_markdown("- **Use Markdown Format**")
        print()
        print_markdown("For example your codes can be like this:")
        print("\n\t```language")
        print("\t\tYour Codes Here")
        print("\t```\n")
    else:
        print_markdown("Markdown mode is off :D")

    while app_alive:
        print_borderized("- **Enter your question and use Ctrl+Enter to send:**")

        user_input=get_input();

        if user_input == False:
            app_alive == False
            break

        print_borderized("# Your Question:")

        print_markdown(user_input);

        print_borderized("# AI Answer:")

        print_markdown("AI Answer here")

        print_markdown("---")

        if input("\n(Enter C to Clear) >> ").upper()=="C":
            clear()

    # clear screen before app ends
    clear()
    print_borderized("# **Bye Bye :D**")

if __name__ == "__main__":
    main()