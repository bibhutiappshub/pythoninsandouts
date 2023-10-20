# Generators are lazy so it's very useful in

def mygenerators():
    yield 1
    yield 2
    yield 3


g = mygenerators()
# first_yieled_val = next(g)
# second_yieled_val = next(g)
# third_yieled_val = next(g)
#
# print(first_yieled_val, second_yieled_val, third_yieled_val)

# We can pass the generators into any builtin function.
print(sorted(g, reverse=True))


def countdown(num):
    print("Starting!!")
    while num > 0:
        yield num
        num -= 1


cd = countdown(5)  # This will not print anything until we use cd
print(next(cd))  # It will show the first yielded value
print(next(cd))  # It will show the second yielded value
print(next(cd))
print(next(cd))
print(next(cd))


# Example of large datasets
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1

    return nums


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


mylist = firstn(10)
print(mylist)
print(sum(firstn(10)))#In this case in that array lot of variables are stored in that array. Takes a lot of memory
print(sum(firstn_generator(10)))#That is not the case here.

# One more advantage of generators is we don't have to wait for all the elements to be
# generated before using this.

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

fib = fibonacci(10)
for i in fib:
    print(i)

# Generator expressions. It's like list compression but instead of [] we use ()
mygenerator = (i for i in range(10) if i % 2 ==0)
print(mygenerator)

for i in mygenerator:
    print(i)
