#!/usr/bin/python3
"""file contains code for console program"""


import re
import sys
import ast
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    '''contains the entry point of the command interpreter'''
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
            "City": City, "State": State, "Amenity": Amenity,
            "Review": Review}

    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    def preloop(self):
        """Prints is isatty false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.
        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Command to also exit the program\n"""
        print()
        exit()
        return True

    def emptyline(self):
        """does nothing when no command is given\n"""
        return False

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it to the JSON file
        and prints the id"""
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        try:
            if not arg:
                raise SynaxError()
            arg_list = arg.split(" ")
            params = {}
            for args in arg_list[1:]:
                arg_attr = args.split("=")
                arg_attr[1] = eval(arg_attr[1])
                if type(arg_attr[1]) is str:
                    arg_attr[1] = (arg_attr[1].
                                   replace("_", " ").replace("\"", '\\"'))
                elif arg_attr[0] in integers:
                    arg_attr[1] = int(arg_attr[1])
                elif arg_attr[0] in floats:
                    arg_attr[1] = float(arg_attr[1])
                params[arg_attr[0]] = arg_attr[1]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class does not exist **")
        new_obj = HBNBCommand.classes[arg_list[0]](**params)
        storage.new(new_obj)
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """prints the string representation of an instance based on
        the classname and id"""
        args = arg.split()  # splits the argument using whitespace
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) > 1:
            key = args[0] + "." + args[1]
            for obj in storage.all().keys():
                if obj == key:
                    print(storage.all()[key])
                    break
            if obj != key:
                print("** no instance found **")

    def count(self, line):
        """
        This counts the instances of a certain class
        """
        cmd_list = line.split('.')
        class_name = cmd_list[0]
        if class_name not in HBNBCommand.classes:
            raise NameError("** class doesn't exist **")
        else:
            counts = 0
            for key in storage.all():
                keyval = key.split(".")[0]
                if keyval == class_name:
                    counts += 1
            print(counts)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        argv = arg.split()  # splits arguments using whitespace as seperator
        if argv[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                key = argv[0] + "." + argv[1]
                storage.all().pop(key)
                storage.save()
            except Exception:
                print("** no instance found **")
            finally:
                return

    def default(self, line):
        """
        This takes care of all self defined functions
        """
        inst_ids = re.search(r'\d[a-z0-9-]+', line)
        if inst_ids:
            inst_id = inst_ids.group(0)
        cmd_list = line.split(".")
        if len(cmd_list) == 2:
            class_name = cmd_list[0]
            if class_name in HBNBCommand.classes:
                if cmd_list[1] == "count()":
                    self.count(class_name)
                elif cmd_list[1] == "all()":
                    self.do_all(class_name)
                elif cmd_list[1][:4] == "show":
                    self.do_show("{} {}".format(class_name, inst_id))
                elif cmd_list[1][:7] == "destroy":
                    self.do_destroy("{} {}".format(class_name, inst_id))
                elif cmd_list[1][:6] == "update":
                    cmd_attrs = line.split(",")
                    if cmd_attrs[1][1] == "{":
                        dict_vals = ast.literal_eval(
                                re.search(r'({.+})', line).group(0))
                        for key, value in dict_vals.items():
                            self.do_update("{} {} {} {}".format(
                                class_name, inst_id, key, value))
                    else:
                        cmd_attr = cmd_attrs[1].strip()
                        cmd_attr1 = cmd_attrs[2].split(")")[0]
                        B
                        self.do_update("{} {} {} {}".format(
                            class_name, inst_id, cmd_attr, cmd_attr1))

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all().items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))

        print(print_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        argv = arg.split()
        if argv[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(argv) == 1:
            print("** instance id missing **")
        else:
            try:
                key = argv[0] + "." + argv[1]
                if key in storage.all():
                    storage.all()[key]
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
                value = argv[3].strip(":\"\'")
            attr = argv[2].strip(":\"\'")
            setattr(storage.all()[key], attr, value)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
