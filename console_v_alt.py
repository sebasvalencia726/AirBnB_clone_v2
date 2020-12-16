#!/usr/bin/python3
""" Console Module """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from shlex import split
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """program called console.py that contains the entry point
    of the command interpreter
    """
    prompt = "(hbnb) "
    total_classes = {"BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"}

    def empty(self):
        """Public method to ignore empty argss"""
        pass

    def do_EOF(self, args):
        """EOF implementation
        """
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel and its inherits classes,
        and saves it (to the JSON file) and prints the id

        Inherit classe:
            User, State, City, Amenity, Place and Review.
        """
        try:
            if not args:
                raise SyntaxError()
            myList = args.split(" ")
            parameters = myList[1:]
            obj = eval("{}()".format(myList[0]))
            for item in parameters:
                key, value = item.split('=')
                if len(value) >= 2 and value[0] is '"':
                    value = value.replace("_", " ")
                    for n in range(len(value)):
                        if n > 0 and value[n] is '"':
                            if value[n-1] is not "\\":
                                n = n + 1
                                value = value[:n]
                                break
                    setattr(obj, key, str(value[1:-1]))
                elif '.' in value:
                    setattr(obj, key, float(value))
                else:
                    setattr(obj, key, int(value))
            obj.save()
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id

        Args:
            args (str): class name and id of the instance.
        """
        try:
            if not args:
                raise SyntaxError()
            myList = args.split(" ")
            if myList[0] not in self.total_classes:
                raise NameError()
            if len(myList) < 2:
                raise IndexError()
            objects = storage.all()
            key = myList[0] + '.' + myList[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and
        id and save the change into the JSON file.

        Args:
            args (str): class name and id to delete.
        """
        try:
            if not args:
                raise SyntaxError()
            myList = args.split(" ")
            if myList[0] not in self.total_classes:
                raise NameError()
            if len(myList) < 2:
                raise IndexError()
            objects = storage.all()
            key = myList[0] + '.' + myList[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name.

        Args:
            args (class): class objects to print.
        """
        objects = storage.all()
        myList = []
        if not args:
            for key in objects:
                myList.append(objects[key])
            print(myList)
            return
        try:
            args = args.split(" ")
            if args[0] not in self.total_classes:
                raise NameError()
            for key in objects:
                name = key.split('.')
                if name[0] == args[0]:
                    myList.append(objects[key])
            print(myList)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and
        id by adding or updating attribute and save the change
        into the JSON file.

        Args:
            args (str): Usage: update <class name>
                           <id> <attribute name> "<attribute value>"
        """
        try:
            if not args:
                raise SyntaxError()
            myList = split(args, " ")
            if myList[0] not in self.total_classes:
                raise NameError()
            if len(myList) < 2:
                raise IndexError()
            objects = storage.all()
            key = myList[0] + '.' + myList[1]
            if key not in objects:
                raise KeyError()
            if len(myList) < 3:
                raise AttributeError()
            if len(myList) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[myList[2]] = eval(myList[3])
            except Exception:
                v.__dict__[myList[2]] = myList[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def count(self, args):
        """count the number of instances
        """
        counter = 0
        try:
            myList = split(args, " ")
            if myList[0] not in self.total_classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == myList[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")

    def default(self, args):
        """Return all instances of a class and the number of instances
        """
        myList = args.split('.')
        if len(myList) >= 2:
            if myList[1] == "all()":
                self.do_all(myList[0])
            elif myList[1] == "count()":
                self.count(myList[0])
            elif myList[1][:4] == "show":
                self.do_show(self.strip_clean(myList))
            elif myList[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(myList))
            elif myList[1][:6] == "update":
                args = self.strip_clean(myList)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, args)

    def strip_clean(self, args):
        """strips the argument and return a string of command
        Args:
            args: input list of args
        Return:
            returns string of argumetns
        """
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

    def default(self, line):
        """retrieve all instances of a class"""
        myList = line.split('.')
        if len(myList) >= 2:
            if myList[1] == "all()":
                self.do_all(myList[0])
            elif myList[1] == "count()":
                self.count(myList[0])
            elif myList[1][:4] == "show":
                self.do_show(self.strip_clean(myList))
            elif myList[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(myList))
            elif myList[1][:6] == "update":
                args = self.strip_clean(myList)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
