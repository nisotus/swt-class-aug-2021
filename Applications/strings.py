# print(movie)
#
# Get single characters from a string
# print(movie[0])
# print(movie[1])
# print(movie[18])
#
# Get single characters from a string in reverse order
# print(movie[-1])
# print(movie[-2])
# print(movie[-19])

# Get multiple characters from a string

# print(movie.find("T"))
# print(movie[:])


# import re
# movie = "The Game of Thrones"
# for m in re.finditer('T',movie):
#          print('T found', m.start())


# name = "Andrew"
# print(name[1:5])


# FORMATTED STRINGS
# *******************************

# How can we print the message (John [Smith] is a coder) to the terminal

first = "John"
last = "Smith"
message = first + " [" + last + "] is a coder"
print(message)

# Using formatted string
msg = f"{first} [{last}] is a coder" # the curly braces are place holders for values of variables
print(msg)

