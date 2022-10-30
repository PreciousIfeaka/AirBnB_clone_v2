#!/usr/bin/python3
<<<<<<< HEAD
"""file contains code for console program"""
=======
<<<<<<< HEAD
"""This module contains a mini shell console
"""
import cmd
import sys
import models
from models.engine.file_storage import FileStorage
from shlex import split
=======
>>>>>>> 007809935c850ffb05bc675957415652752ecaa9

import models
import cmd
import shlex
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
<<<<<<< HEAD
from datetime import datetime

classes = ["BaseModel", "User", "State", "Amenity", "City", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    """This class contains the command interpreter"""

    prompt = '(hbnb) '
    file = None
=======

classes = ["BaseModel", "User", "Place", "City", "State", "Amenity", "Review"]


class HBNBCommand(cmd.Cmd):
    '''contains the entry point of the command interpreter'''
    prompt = '(hbnb) '

<<<<<<< HEAD
=======
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa

>>>>>>> 007809935c850ffb05bc675957415652752ecaa9
    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
<<<<<<< HEAD
        """Command to also exit the program\n"""
        return True

    def emptyline(self):
        """does nothing when no command is given\n"""
        return False

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it to the JSON file
        and prints the id"""
        args = arg.split()  # splits the argument using whitespace
        if len(args) < 1:
            print("** class name missing **")
            return False
        if args[0] not in classes:
            print("** class doesn't exist **")
            return False
        else:
            new_instance = eval(args[0] + "()")
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """prints the string representation of an instance based on
        the classname and id"""
        args = arg.split()  # splits the argument using whitespace
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) > 1:
            key = args[0] + "." + args[1]
=======
        """Exits the program\n"""
        return True

    def emptyline(self):
        """does nothing if no command is given"""
        return False

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        argv = arg.split()  # splits using whitespace to give arguments
        if argv[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_inst = eval(argv[0] + "()")
            print(new_inst.id)
            new_inst.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        argv = arg.split()
        if argv[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(argv) < 2:
            print("** instance id missing **")
            return
        elif len(argv) > 1:
            key = argv[0] + "." + argv[1]
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")
                return

    def do_destroy(self, arg):
<<<<<<< HEAD
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) == 2:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()
                return

    def do_all(self, arg):
        if not arg:
            lists = []
            try:
                for key, value in models.storage.all().items():
                    lists.append(str(value))
                print(lists)
            except Exception:
                pass
        else:
            args = arg.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            lists = []
            if len(args) == 1 and args[0] in classes:
                for key, value in models.storage.all().items():
                    if key.split(".")[0] == args[0]:
                        lists.append(str(value))
                if not lists:
                    return
                print(lists)

    def do_update(self, arg):
        args = arg.split()
        key = args[0] + "." + args[1]
        if len(args) == 0:
            print("** class name is missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            if not models.storage.all()[key]:
                print("** no instance found **")
        objects = models.storage.all()
        obj = objects[key]
        immutables = ["id", "created_at", "updated_at"]
        if obj:
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            elif args[2] not in immutables:
                try:
                    obj.__dict__[args[2]] = eval(args[3])
                except Exception:
                    obj.__dict__[args[2]] = args[3]
                    obj.save()

    def count(self, line):
        """
        This counts the instances of a certain class
        """
        cmd_list = split(line, ".")
        class_name = cmdi_list[0]
        if class_name not in classes:
            raise NameError("** class doesn't exist **")
        else:
            counts = 0
            for key in models.storage.all():
                keyval = key.split(".")[0]
                if keyval == class_name:
                    counts += 1
            print(counts)

    def default(self, line):
        """
        This takes care of all slef defined functions
        """
        cmd_list = line.split(".")
        if len(cmd_list) == 2:
            class_name = cmd_list[0]
            if class_name in classes:
                if cmd_list[1] == "count()":
                    self.count(class_name)
                elif cmd_list[1] == "all()":
                    self.do_all(class_name)
                elif cmd_list[1][:4] == "show":
                    inst_id = cmd_list[1][6:42]
                    self.do_show("{} {}".format(class_name, inst_id))
=======
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        argv = arg.split()  # splits arguments using whitespace as seperator
        if argv[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(arg) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                key = argv[0] + "." + argv[1]
                models.storage.all().pop(key)
                models.storage.save()
            except Exception:
                print("** no instance found **")
            finally:
                return

    def do_all(self, arg):
        '''Prints all string representation of all instances based or
        not on the class name'''
        if not arg:
            list_inst = []
            for key, val in models.storage.all().items():
                list_int.append(str(val))
            if not list_inst:
                print("storage is empty!")
                return
            else:
                print(list_inst)
                return
        argv = arg.split()
        if argv[0] not in classes:
            print("** class doesn't exist **")
            return
        else:
            list_inst = []
            for key, val in models.storage.all().items():
                if str(key.split('.')[0]) == argv[0]:
                    list_inst.append(str(val))
            if not list_inst:
                return
            else:
                print(list_inst)
                return

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        argv = shlex.split(arg)
        if argv[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(argv) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = argv[0] + "." + argv[1]
                if key in models.storage.all():
                    models.storage.all()[key]
            except Exception:
                print("** no instance found **")
                return
        if len(argv) == 2:
            print("** attribute name missing **")
            return
        elif len(argv) == 3:
            print("** value missing **")
            return
        else:
            key = argv[0] + "." + argv[1]
            try:
                try:
                    value = int(argv[3])
                except ValueError:
                    value = float(argv[3])
            except ValueError:
                value = argv[3].strip(":\"'")
            attr = argv[2].strip(":\"'")
            setattr(models.storage.all()[key], attr, value)
            models.storage.save()
>>>>>>> 80865b320f4c07f10c52f1d58b658776ca3c42fa


if __name__ == '__main__':
    HBNBCommand().cmdloop()
