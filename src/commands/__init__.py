from os import walk

f = []
commands = {}


# Make a list of command names
for (dirpath,dirnames,filenames) in walk("commands"):
    if dirpath == "commands":
        f.extend(filenames)
f.remove("__init__.py")

# Import each of them and populate the commands dictionary
for each in f:
    cm = each[:len(each)- 3] # Truncate the .py at the end
    exec(f"from .{cm} import *")
    commands[cm] = (eval(f"{cm}.main"), eval(f"{cm}.description"))

