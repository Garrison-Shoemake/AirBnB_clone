#!/usr/bin/python3
""" This is the Console file """


import cmd
import string, sys


class HBNBCommand(cmd.Cmd):
    """ this class defines the console class """

    prompt = "(hbnb)"

    def do_EOF(self, notself):
        print()
        return True


    def do_quit(self):
        """ Exits (hbnb) console """
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
