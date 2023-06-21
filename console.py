#!/usr/bin/python3
"""Class for console of HBNB"""

import cmd
import json
from models.engine.file_storage import FileStorage
from models.engine.file_storage import ObjectEncoder
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    intro = ""
    prompt = "(hbnb)  "

    def class_exists(self, cls):
        """checks whether the class do exist"""

        available_classes = [
            "BaseModel",
            "User",
            "Amenity",
            "City",
            "Place",
            "Review",
            "State"
        ]
        return cls in available_classes

    def parameters(self, command):
        """Parameters splitter"""

        lst = command.split(" ")
        return lst

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):
        """Command for user interrupt with CTRL+C"""

        return True

    def do_create(self, arg):
        """create <class_name>"""

        args = arg.split()
        keys = []
        values = []
        attributes = {}
        for arg in args:
            if "=" in arg:
                val = arg.split('=')
                """ check if it a string """
                key_length = len(val[1])
                value = val[1]
                if(value[0] == "\"" and value[key_length - 1] == "\""):
                    """ This is a string"""
                    keys.append(val[0])
                    value = value[1:key_length - 1]
                    value = value.replace("\"", "\\\"")
                    value = value.replace("\'", "\\\'")
                    value = value.replace("_", " ")
                    values.append(value)
                    attributes[val[0]] = value
                elif "." in value:
                    """ this is a float """
                    keys.append(val[0])
                    values.append(float(val[1]))
                    attributes[val[0]] = val[1]

                elif value.isnumeric():
                    """ this is an integer """
                    keys.append(val[0])
                    values.append(int(val[1]))
                    attributes[val[0]] = val[1]
        """ create a new instance as seen below """
        new_class = type(args[0], (BaseModel, ), attributes)
        instance = new_class()
        """ for key in attributes.keys():
            setattr(instance, key, attributes[key]) """
        print(instance.id)
        storage.new(instance)
        storage.save()
        return
        if len(objects):
            cls = globals()[args[0]]
            instance = cls()
            index = 0
            for key in keys:
                instance[key] = values[index]
                index += 1
            print(instance)
            return
        """print(keys)
        print(values)
        return"""
        if len(arg) == 0:
            print("** class name missing **")
        elif not self.class_exists(arg):
            print("** class doesn't exist **")
        else:
            """cls = globals()[arg]"""

            cls = globals()[arg]
            instance = cls()
            print(instance.id)
            storage.new(instance)
            storage.save()

    def do_show(self, arg):
        """show <class_name> <id>"""

        parameters = self.parameters(arg)

        if len(parameters) > 1:
            uid = parameters[1]
        else:
            uid = ""
        if len(parameters) > 0:
            arg = parameters[0]
        else:
            arg = ""
        instances = storage.all()
        instance_key = arg+"."+uid

        if not len(arg):
            print("** class name missing **")
        elif not self.class_exists(arg):
            print(arg)
            print("** class doesn't exist **")
            print('hello')
        elif not len(uid):
            print("** instance id missing **")
        elif instance_key not in instances.keys():
            print("** no instance found **")
        else:
            print(instances[instance_key])

    def do_destroy(self, cls="", uid=""):
        """destroy <class_name> <id>"""

        parameters = self.parameters(cls)

        if len(parameters) > 1:
            uid = parameters[1]
        else:
            uid = ""
        if len(parameters) > 0:
            cls = parameters[0]
        else:
            cls = ""

        instances = storage.all()
        instance_key = cls+"."+uid

        if not len(cls):
            print("** class name missing **")
        elif not self.class_exists(cls):
            print("** class doesn't exist **")
        elif not len(uid):
            print("** instance id missing **")
        elif instance_key not in instances.keys():
            print("** no instance found **")
        else:
            del instances[instance_key]
            storage.save()

    def do_all(self, arg):
        """show all instances"""

        instances = storage.all()
        objects = []
        if arg and not self.class_exists(arg):
            print("** class doesn't exist **")
        elif len(arg):
            for key in instances.keys():
                if arg == key.split(".")[0]:
                    """print(ObjectEncoder().encode(instances[key]))"""
                    objects.append(ObjectEncoder().encode(instances[key]))
        else:
            for key in instances.keys():
                """print(json.dumps(instances[key]))"""
                objects.append(json.dumps(instances[key]))
        print(objects)

    def do_update(self, cls, uid="", attribute="", new_value=""):
        """update <class_name> <id> <attribute> <new_value>"""
        parameters = self.parameters(cls)

        if len(parameters) > 3:
            cls = parameters[0]
            uid = parameters[1]
            attribute = parameters[2]
            new_value = parameters[3]
        elif len(parameters) > 2:
            cls = parameters[0]
            uid = parameters[1]
            attribute = parameters[2]
            new_value = ""
        elif len(parameters) > 1:
            cls = parameters[0]
            uid = parameters[1]
            attribute = ""
            new_value = ""
        elif len(parameters) > 0:
            cls = parameters[0]
            uid = ""
            attribute = ""
            new_value = ""
        else:
            cls = ""
            uid = ""
            attribute = ""
            new_value = ""

        instances = storage.all()
        instance_key = cls + "." + uid

        if not len(cls):
            print("** class name missing **")
        elif not self.class_exists(cls):
            print("** class doesn't exist **")
        elif not len(uid):
            print("** instance id missing **")
        elif instance_key not in instances.keys():
            print("** no instance found **")
        elif not len(attribute):
            print("** attribute name missing **")
        elif not len(new_value):
            print("** value missing **")
        else:
            exceptions = ['id', 'created_at', 'updated_at']
            allowed_types = [type("hello"), type(1), type(2.3)]
            if attribute not in exceptions:
                if type(new_value) in allowed_types:
                    instances[instance_key][attribute] = new_value
                    storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
