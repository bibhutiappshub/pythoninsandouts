# Variable arguments

# *args : We can pass any number of positional arguments to a function. It's a tuple.
# **kwargs : We can pass any number of keyword arguments to a function. It's a dictionary.
def foo(a, b, *args, **kwargs):
    print(a, b)

    for param in args:
        print(param)

    for key in kwargs:
        print(key, kwargs[key])

foo(5, 10, 3, 4, 5, six=6, seven=7)


# Unpacking arguments
def bar(a, b, c):
    print(a, b, c)

mylist = [1, 2, 3]
my_dict = {"a":10, "b":20, "c":3}
bar(*mylist)
bar(**my_dict) # the keys should match parameters name and also it should have same num of elements.

# Local and global variables
def foobar():
    global number
    x = number
    number = 3
    print("number inside function:", x)

number = 0
foobar()
print(number)

# Call by value and call by reference.

def foofunc(x):
    x = 5

def foolist(a_list):
    a_list.append("Hi")

var = 10
foofunc(var) #It is immutable and is passed
print(var)

mysamplelist = ["Hello"]
foolist(mysamplelist)
print(mysamplelist)