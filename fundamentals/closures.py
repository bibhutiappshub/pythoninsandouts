# A closure is a inner function which remembers or has access to the variables in the local
# scope where it was created even after the outer function finished it's execution before.
# It's called Closures because it closes over the free variables from their environment.

def outer_function1():
    message = "Hello"

    def inner_func1():
        print(message)

    # return inner_func() # In this line we are executing the function and then return
    return inner_func1


inner_func_var = outer_function1()
inner_func_var()
inner_func_var()
inner_func_var() # We can still access message even the outer_function() is executed earlier.
                 # So it still remembers the message variable. This is what the Closure is.

def outer_function2(msg):
    message = msg

    def inner_func2():
        print(message)

    # return inner_func() # In this line we are executing the function and then return
    return inner_func2


inner_func_var1 = outer_function2("Hi")
inner_func_var2 = outer_function2("Hello")
inner_func_var1()
inner_func_var2()
inner_func_var1()
