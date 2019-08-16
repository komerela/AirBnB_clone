#!/usr/bin/python3
"""This is the console for AirBnB"""
import cmd
import json
import shlex
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """this class is entry point of the command interpreter
    """
    prompt = ("(hbnb) ")
    """
    all_classes = {"BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"}
    """

    def emptyline(self):
        """
        Ignores empty spaces
        """
        pass

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        Quit command to exit the program at EOF input
        """
        return True

    def do_create(self, args):
        """
        create <Class name> <param 1> <param 2>...
        Creates an instance of the class from command line input arg and param
        e.g.
        create State name="California"
        State.create(name="California")
            type string => <key name>=<"value"> Value starts with double quotes
            type float => <unit>.<decimal>
            type integer => <number>
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args, posix=False)
            new_instance = eval(args[0])()
            if len(args) > 1:
                for a in range(1, len(args)):
                    key, value = args[a].split('=')
                    if value[0] == '"' and val[len(val) - 1 == '"':
                        value == value[1:len(val) - 1]
                    "
                            value = value.replace('_', ' ')
                            value = str(value)
                            elif isinstance(eval(value), float):
                            value = float(value)

                            elif isinstance(eval(value), int):
                            value = int(value)

                            else:
                            continue

                            setattr(new_instance, key, value)

                            new_instance.save()
                            print(new_instance.id)

                            except Exception as e:
                            print(e)
                            print("** class doesn't exist **")

    def do_show(self, args):
    """
    Prints the string representation of an instance
    """
        args= shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage= FileStorage()
        storage.reload()
        my_dict= storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key= args[0] + "." + args[1]
        key= args[0] + "." + args[1]
        try:
            val= my_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
    """
    Deletes an instance based on the class name and id
    """
        args= shlex.split(args)

        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_name= args[0]
        class_id= args[1]
        storage= FileStorage()
        storage.reload()
        my_dict= storage.all()

        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        key= class_name + "." + class_id
        try:
            del my_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_all(self, args):
    """Prints all string representation of all instances
    Exceptions:
    NameError: when there is no object taht has the name
    """
    my_list= []
    objects= models.storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    my_list.append(val)
            else:
                my_list.append(val)
        print(my_list)

    def do_update(self, line):
    """
    Updates an instanceby adding or updating attribute
    """
    storage= FileStorage()
    storage.reload()
    args= shlex.split(args)
    if len(args) == 0:
        print("** class name missing **")
        return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key= args[0] + "." + args[1]
        my_dict= storage.all()
        try:
            obj_val= my_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type= type(getattr(obj_val, args[2]))
            args[3]= attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_val, args[2], args[3])
        obj_val.save()

    def count(self, args):
        """
        count the number of instances of a class
        """
        my_list= []
        storage= FileStorage()
        storage.reload()
        objects= storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    my_list.append(val)
            else:
                my_list.append(val)
        print(len(my_list))

    """
    def strip_clean(self, args):
        strips the argument and return a string of command
        Args:
            args: input list of args
        Return:
            returns string of argumetns

        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)
    """

    def default(self, args):
        """
        Checks for the function names not even covered
        """
        functions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except:
            print("*** Unknown syntax:", args[0])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
