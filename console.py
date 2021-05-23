#!/usr/bin/python3
""" This is the Console file """

import string
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage

classes = {'BaseModel': BaseModel}

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

        if len(split) == 0:
            print("** class name missing **")
            return
        elif split[0] not in classes:
            print("** class doesn't exist **")
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

    def do_destroy(self, *args):
        """ Deletes an instance based on class name and id
        Example: <class_name> <id>
        """
        # class name not exist : ** class doesn't exist **
        # class / id no match : ** no instance found **
        command = self.parseline(args[0])
        command2 = command[2]
        split = command2.split()

        if len(split) == 0:
            print("** class name missing **")
            return
        elif split[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(split) == 1:
            print("** instance id missing **")
            return

        class_name = split[0]
        id_num = split[1]
        objects = storage.all()
        if split[0] not in classes:
            print("** class doesn't exist **")
        for i in objects.keys():
            if i == '{}.{}'.format(class_name, id_num):
                del(objects[i])
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, *args):
        """Prints all classes of given <class name>
        if no <class name> given, prints all classes
        Example: all
        Example: all <class name>
        """

        command = self.parseline(args[0])
        command2 = command[2]
        split = command2.split()
        # if class given, only show those:
        # otherwise, show all
        objects = storage.all()

        if len(split) == 0:
            print([str(objects)])
            return
        elif split[0] in classes:
            for i in objects.keys():
                if i.startswith(split[0]):
                    print([str(objects[i])])
        else:
            print("** class doesn't exist **")

    def do_update(self, *args):
        """ """
        command = self.parseline(args[0])
        command2 = command[2]
        split = command2.split()
        objects = storage.all()

        if len(split) == 0:
            print("** class name missing **")
            return
        if len(split) == 1:
            if split[0] not in classes:
                print("** class doesn't exist **")
                return
            else:
                print("** instance id missing **")
                return
        if len(split) == 2:
            print("** attribute name missing **")
            return
        if len(split) == 3:
            print("** value missing **")
            return

        else:
            obj = split[0] + '.' + split[1]
            for i in objects.keys():
                if i == split[3]:
                    print("Match found!")
                    # might need new classes with updateable information before testing
                    storage.save()
                else:
                    print("** no instance found **")
                    return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
