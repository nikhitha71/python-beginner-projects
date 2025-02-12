"""
Starting a beginner Python project by Nikhitha
Madlibs using string concatenation
"""
# # suppose we want to create a string that says "coding with _____ "
#name = "Nikhitha"

# # a few ways to do this
#print("Coding with " + name)
#print("Coding with {}".format(name))
#print(f"Coding with {name}")

# Taking user inputs
adj = input("adjective: ")
verb = input("verb: ")

# Creating the Mad Lib
madlib = f"Computer programming is so {adj}! It makes me excited all the time because \
I love to {verb}. It's like a passion!"

# Printing the Mad Lib
print(madlib)


