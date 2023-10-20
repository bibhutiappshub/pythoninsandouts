from functools import reduce

# Lambda declaration
double_lambda = lambda num: num * 2

multiply = lambda a, b: a * b
print(multiply(2, 3))

# map(), filter() and reduce()
def triple(num):
    return num * 3


my_list = [1, 2, 3]
double_result = map(lambda num: num * 2, my_list)
triple_result = map(triple, my_list)

print(list(double_result))
print(list(triple_result))

filter_result = filter(lambda num: num % 2 == 0, my_list)
print(list(filter_result))

expenses = [("Dinner", 50), ("Travel", 80)]
reduce_result = reduce(lambda a, b: a[1]+b[1], expenses)
print(reduce_result)

points2D = [(1, 2), (5, -1), (15, 1), (10, 4)]
sorted_points = sorted(points2D, key=lambda x: x[1])  # Sort by second element of the tuple
print(points2D)
print(sorted_points)

