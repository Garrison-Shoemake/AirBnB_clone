#!/usr/bin/python3
""" This is the Console file """

import string
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage

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
        """ Creates a new instance of <model name>
        Example: (hbnb) create <model name> """
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

    def do_show(self, *args):
        """ Prints a string representation based on class and id
        Example: (hbnb) show <class name> <id> """
        command = self.parseline(args[0])
        command2 = command[2]
        split = command2.split()
        print(len(split))
        if len(split) == 0:
            print("** class name missing **")
            return
        elif len(split) == 1:
            print("** instance id missing **")
            return
        class_name = split[0]
        id_num = split[1]
        # involves comparing to class data for confirmation:
        objects = storage.all()
        for i in objects.keys():
            if i == '{}.{}'.format(class_name, id_num):
                print(objects[i])
                return
        print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
