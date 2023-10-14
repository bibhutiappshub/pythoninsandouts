# Decorators allows users to modify the behaviours of the function
# without changing the function code.

def loghello(func):
    def wrapper():
        print("Before Hello")
        funcval = func()
        print("After Hello")
        return funcval
    return wrapper

@loghello
def hello():
    print("Hello")

hello()
