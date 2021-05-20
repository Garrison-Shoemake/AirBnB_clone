#!/usr/bin/python3
""" This is the Console file """


import cmd
import string, sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ this class defines the console class """

    prompt = "(hbnb)"

    def do_EOF(self, notself):
        print()
        return True

    def do_quit(self, notself):
        """ Exits (hbnb) console """
        return True

    def emptyline(self):
        pass

    def do_create(self, class_name):
        if not class_name:
            print("** class name missing **")
            return
        if class_name == 'BaseModel':
            new_class = BaseModel()
            new_class.save()
            print(new_class.id)
            return
        else:
            print("** class doesn't exist **")
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
