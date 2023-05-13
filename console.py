#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """ Class for console of HBNB """

    intro = ""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """ Quit command to exit the program """

        return True

    def do_EOF(self, arg):
        """ Command for user interrupt with CTRL+C """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
