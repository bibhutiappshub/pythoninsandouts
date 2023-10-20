import operator
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import accumulate
from itertools import groupby

# product does a cartesian product
a = [1, 2]
b = [3, 4]
pd = product(a, b)
print(list(pd))

# Calculate the permutations
a = [1, 2, 3]
perm = permutations(a)
perm_2 = permutations(a, 2)
print(list(perm))
print(list(perm_2))

# Calculate combinations
b = [1, 2, 3]
comb = combinations(b, 2)
combs_with_replacement = combinations_with_replacement(b, 2)
print(list(combs_with_replacement))

# Accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
mul_acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))
print(list(mul_acc))

# groupby
persons = [{"name": "Tim", "age": 25}, {"name": "Dan", "age": 25}, {"name": "Lisa", "age": 26},
           {"name": "Claire", "age": 26}, {"name": "Matthew", "age": 27}]

groupbyobj = groupby(persons, key=lambda x: x["age"])
for key, value in groupbyobj:
    print(key, " ", list(value))
