def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)

# tail recursion
def tail_factorial(num):

    def tail_factorial_helper(acc, num):
        if num == 1:
            return acc

        return tail_factorial_helper(acc * num, num-1)

    return tail_factorial_helper(1, num)


print(factorial(3))
print(tail_factorial(3))
