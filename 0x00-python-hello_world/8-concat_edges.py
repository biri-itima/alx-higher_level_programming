#!/usr/bin/python3
str = "Python is an interpreted, object-oriented programming\nlanguage that combines remarkable power with very clear syntax"
str = str[str.find("object"): str.find("\n")] + " " + str[str.find("with"): str.find("very")]
str = str + "python"
print(str)
