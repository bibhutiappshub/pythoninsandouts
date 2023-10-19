# Lists are ordered, mutable and allow duplicated elements

my_list = ["Mango", "Cherry", "Banana"]
print(my_list)

# Retrieving list elements
print(my_list[0])

# Find length of the list
print(len(my_list))

# Looping lists
for item in my_list:
    print(item)

# Check if the item is inside the list
if "apple" in my_list:
    print("Present!!")
else:
    print("Not Present!!")

# Adding items into list
my_list.append("Apple") # This will add items at the end of the list.
print(my_list)

# Want to add items at a specific position
my_list.insert(2,"Chiku")
print(my_list)

# Removing items from list
popped_item = my_list.pop() # It returns the last element by removing it.
print(popped_item)

# Reverse the list by reverse method
reversed_list = my_list.reverse()
print(reversed_list)

# Sorting lists
num_list = [5, 8, 11, 2, 1]
num_list.sort() #This will sort the list in ascending order and change the list itself.
num_list.sort(reverse=True) #This will sort the list in descending order.
sorted_list = sorted(num_list, reverse=True) #This will sort and return the new list.
print(num_list)
print(sorted_list)

# Create a list with repeated items
rep_list = [1, 2, 3] * 3
print(rep_list)

# Merge 2 lists
merged_list = num_list + rep_list
print(merged_list)

# Substring of a list
sliced_list = merged_list[2:4] # From start to end - 1
sliced_list1 = merged_list[2:] # From 2 to end
sliced_list2 = merged_list[:4] # From start to 4
sliced_list3 = merged_list[1::2] # This will return every alternate element starting from index 1
sliced_list4 = merged_list[::-1] # This will return every element from end, which actually reverse it
print(sliced_list)
print(sliced_list1)
print(sliced_list2)
print(sliced_list4)

# Copying a list
list_original = ["Banana", "Apple", "Blueberry"]
list_shallow_copy = list_original # Here if we change one it's reflected for other one
list_copy1 = list_original.copy()
list_copy2 = list_original[:]
list_copy3 = list(list_original)
list_original.sort()
print(list_original)
print(list_shallow_copy)
print(list_copy1)
print(list_copy2)
print(list_copy3)

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

# Clear all the elements from the list
my_list.clear()
print(my_list)