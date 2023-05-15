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
        if arg and not self.class_exists(arg):
            print("** class doesn't exist **")
        elif len(arg):
            for key in instances.keys():
                if arg == key.split(".")[0]:
                    print(ObjectEncoder().encode(instances[key]))
        else:
            for key in instances.keys():
                print(json.dumps(instances[key]))

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
