class MyClass:
    def __init__(self, name):
        self.name = name


# Creating an instance of MyClass
my_object = MyClass("Example")

# Creating the dictionary
my_dict = {}

# Inserting objects into the dictionary
my_dict['obj1'] = my_object
my_dict['greeting'] = "Hello, world!"
my_object = MyClass("butts")

my_dict['obj1'] = my_object

# Accessing and printing a value from the dictionary
print(my_dict['obj1'].name)  # Output: Example
print(my_dict['greeting'])   # Output: Hello, world!
