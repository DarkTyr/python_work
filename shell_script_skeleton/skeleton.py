# -*- coding: utf-8 -*-

# System level imports
#import cmd2 as cmd
import cmd
import sys
import os

'''
The Idea here with this script is to create an command line shell script that a user 
can interact with to manipulate a device (AKA DSP System). This needs to have/support
multiple menu levels with multiple actions per menu level. This also needs to be able
to move up and down the menu levels freely. 

The idea starting below is based on this stackOverflow post
https://stackoverflow.com/questions/3966187/how-to-do-a-multi-level-cli-in-python
'''


'''
The below def print_* methods give the ability to write colored text to the console.
This is really useful for displaying information and debugging.
'''
def print_uheader(text):
    print('\033[4m' + '\033[95m' + text + '\033[0m' + '\033[0m')

def print_magenta(text):
    print('\033[95m' + text + '\033[0m')

def print_green(text):
    print('\033[92m'  + text + '\033[0m')

def print_blue(text):
    print('\033[94m' + text + '\033[0m')

def print_norm(text):
    print(text)

def print_yellow(text):
    print('\033[93m' + text + '\033[0m')

def print_red(text):
    print('\033[91m' + text + '\033[0m')

def format_uheader(text):
    return ('\033[4m' + '\033[95m' + text + '\033[0m' + '\033[0m')

def format_magenta(text):
    return ('\033[95m' + text + '\033[0m')

def format_green(text):
    return ('\033[92m'  + text + '\033[0m')

def format_blue(text):
    return ('\033[94m' + text + '\033[0m')

def format_norm(text):
    return (text)

def format_yellow(text):
    return ('\033[93m' + text + '\033[0m')

def format_red(text):
    return ('\033[91m' + text + '\033[0m')

# Clear the terminal, there is a minor difference between linux and windows so it
# got wrapped into a definition
def clear_cli():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')
    return

'''
Because I would like to support Py 2.7 and Py 3.7 in some form I decided to wrap the
user input call because they are a bit different. 
'''
def grab_user_input(prompt):
    # return input(prompt)    # Python 3+
    return raw_input(prompt)  # Python 2.7

'''
This is where the command line shell script actually starts. We start by defining the
lowest submenu classes and then working our way up to the top level/main menu.
'''
class SubInterpreter(cmd.Cmd):
    prompt = '(level2) \n'

    def do_subcommand_1(self, args):
        pass

    def do_subcommand_2(self, args):
        pass

    def do_quit(self, args):
        return True
    do_EOF = do_quit

class MyInterpreter(cmd.Cmd):
    prompt = format_magenta('''
    Top level Menu 
        1 : Nothing
        2 : SubMenu
        3 : Nothing''') + format_red('''

         >>  
        ''')

    intro = format_green('Welcome to the Skeleton Sheel Script for Python')

    def do_1(self, args):
        print_blue('Top Level : level1')

    def do_2(self, args):
        sub_cmd = SubInterpreter()
        sub_cmd.cmdloop()

    def do_3(self, args):
        print_blue('Top Level : level3')
    
    def do_exit(self, args):
        sys.exit()

    # def emptyline():
    #     pass

MyInterpreter().cmdloop()