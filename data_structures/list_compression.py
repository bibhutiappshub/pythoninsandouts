# List compressions are preferred over loops as the operation can be
# done using the single line.

# Suppose we want to make a new list by with power of 2 ofthe following list.
# Then we can do it 2 ways. By using loops or by list compression.

num_list = [2, 3, 4, 5]
new_num_list = []

# Method-1
for num in num_list:
    new_num_list.append(num**2)

print(new_num_list)

# Method-2
compressed_list = [num ** 3 for num in num_list]
print(compressed_list)

# Method-3
mapped_list = list(map(lambda n: n**4, num_list))
print(mapped_list)