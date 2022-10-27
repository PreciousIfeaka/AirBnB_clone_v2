#!/c/msys64/mingw64/bin/python

import models
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review

classes = ["BaseModel", "User", "Place", "City", "State", "Amenity", "Review"]

class HBNBCommand(cmd.Cmd):
    '''contains the entry point of the command interpreter'''
    prompt = '(hbnb) '


    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
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
        argv = arg.split() #splits using whitespace to give arguments
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
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")
                return

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        argv = arg.split() #splits arguments using whitespace as seperator
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
            except:
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
            except:
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
