# Sets are unordered, mutable and doesn't contain any duplicate values.
myset = {1, 2, 3, 4, 2}
print(myset)

mynewset = set([5, 4, 3, 2, 5])
print(mynewset)

alphabetset = set("Hello") # In this case the String is represented as list of characters.
print(alphabetset)

# Create an empty set
empty_set = {} # If we create like this, then it will be a empty dictionary.
empty_set = set()
print(empty_set)

# Add and remove elements in a set
myset.add(5)
myset.add(8)
myset.add(10)
myset.remove(8)
print(myset)

# Loop through Sets
for i in myset:
    print(i)

if 1 in myset:
    print("Yes")

# Union and intersection of sets
prime_nums = {2, 3, 5, 7}
odd_nums = {1, 3, 5, 7}
even_nums = {2, 4, 6, 8}

u = odd_nums.union(even_nums)
print(u)

pu = prime_nums.intersection(even_nums)
print(pu)

du = prime_nums.difference(even_nums)
print(du)

sdu = prime_nums.symmetric_difference(even_nums)
print(sdu)

