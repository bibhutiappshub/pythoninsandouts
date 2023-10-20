# Decorators allows users to modify the behaviours of the function
# without changing the original function code.

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

# There are two different decorators. Function decorators and Class decorators.
def incrementbyfive(func):
    def inner_wrapper(*args, **kwargs):
        print("Before increment function")
        result = func(*args, **kwargs)
        print("After increment function")
        return result

    return inner_wrapper


@incrementbyfive
def increment_by_five(x):
    return x + 5


print(increment_by_five(5))


# Decorators with arguments
def say_hello_to_bibhuti(*args, **kwargs):
    def inner_wrapper(func):
        for _ in range(kwargs["num_times"]):
            func()

    return inner_wrapper


@say_hello_to_bibhuti(num_times=5)
def hello_to_bibhuti():
    print(f"Hello Bibhuti!!!")

hello_to_bibhuti


def greet_people(num_times):
    def greet_people_decorator(func):
        def inner_wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)

        return inner_wrapper

    return greet_people_decorator
@greet_people(num_times=5)
def greet(name):
    print(f"Hoi {name}!!!")


greet("Soumya")


