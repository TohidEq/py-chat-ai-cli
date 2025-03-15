#!/usr/bin/env python

from os import system, name
from rich.console import Console
from rich.markdown import Markdown
import keyboard



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





def main():
    clear()

    console = Console()
    #md = Markdown("result of chat here")
    #console.print(md)


    app_alive = True
    console.print(Markdown("---"));
    console.print(Markdown("- **Use Markdown Format**"))
    print()
    console.print(Markdown("For example your codes can be like this:"))
    print("\n\t```language")
    print("\t\tYour Codes Here")
    print("\t```\n")

    while app_alive:
        console.print(Markdown("---"));
        console.print(Markdown("- **Enter your question and use Ctrl+Enter to send:**"))
        console.print(Markdown("---"));

        user_input=get_input();

        if user_input==False:
            app_alive==False
            break

        console.print(Markdown("---"));
        console.print(Markdown("# Your Question:"))
        console.print(Markdown("---"));

        console.print(Markdown(user_input));

        console.print(Markdown("---"));
        console.print(Markdown("# AI Answer:"))
        console.print(Markdown("---"));

        console.print(Markdown("AI Answer here"))

        console.print(Markdown("---"));

        if input("\n(Enter C to Clear)>> ").upper()=="C":
            clear()

    # clear screen before app ends
    clear()
    console.print(Markdown("---"));
    console.print(Markdown("# **Bye Bye :D**"))
    console.print(Markdown("---"))

if __name__ == "__main__":
    main()