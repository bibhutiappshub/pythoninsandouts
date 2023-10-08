# Parameters to a function is passed by references in Python

# Int is immutable. So any changes inside this function will not affect outside.
def check_immutability(int_arg):
    int_arg = 5


int_param = 10
check_immutability(int_param)
print(int_param) # It will print 10

# Dictionary is mutable. So any changes inside this function will affect outside.
def check_mutability(dict_arg):
    dict_arg["name"] = "Sendha"


my_dict = {"name":"Bapi"}
print(my_dict) # It will print {"name":"Bapi"}
check_mutability(my_dict)
print(my_dict) # It will print {"name":"Sendha"}

# Nested Functions
# We need this because sometimes we want a function to hide it's functionality local to it's function.
# If it is not useful outside

def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(" ")
    for word in words:
        say(word)

talk("Say Hello to My Friend")

def count():
    count = 0
    def increment():
        nonlocal count
        count = count+3 # We can't use this directly without declaring count as nonlocal in this scope
                        # By using nonlocal it indicates that this variable is not local to this func
        print(count)

    increment()

count()
