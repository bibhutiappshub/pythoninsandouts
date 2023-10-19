import sys
import timeit

# Tuples are ordered, immutable and allow duplicated elements.
# To declare a tuple it should have parenthesis and separated by comma
not_a_tuple = ("Hello") # This is not a tuple rather than a string
print(tuple, type(tuple))
my_tuple = ("Hi", 28, 28.35, True)
print(my_tuple, type(my_tuple))

# We can create tuples from "tuple" builtin function
my_tuple = tuple(["Hello", 10, False])
print(my_tuple)

# Accessing tuple elements
item = my_tuple[1]
print(item)

# my_tuple[0] = "Bye" # This is not possible as tuplem is immutable

# Loop through tuples
for item in my_tuple:
    print(item)

# Existence of element in tuple
if False in my_tuple:
    print("Exists!!!")
else:
    print("Not Exists!!!")

# Count elements, length of tuple, find index of element inside tuple
letter_tuple = ('a', 'a', 'c', 'b', 'c', 'd', 'c', 'e')
print(len(letter_tuple))
print(letter_tuple.count('c'))
print(letter_tuple.index('b'))

# Convert a tuple into a list
converted_list = list(letter_tuple)
converted_tuple = tuple(converted_list)
print(converted_list)
print(converted_tuple)

# Slicing tuples
sliced_tuples = converted_tuple[2:5]
print(sliced_tuples)

# Unpacking tuples
member_tuple = ("Bibhuti", 35, "Jajpur")
student_tuple = ("Bibhuti", 7.5, 8.0, 8.8, "Jajpur")
copy_member_tuple = member_tuple
print(copy_member_tuple)
name, age, city = member_tuple
name, *cgpa, city = student_tuple
print(name, " ", age, " ", city)
print(name, " ", cgpa, " ", city) # Here cgpa will be a list

# Tuple are more efficient than lists. It takes less memory as well as creation time than list.
# So while iteration tuple is more efficient than list.

same_list = [1, 3, "Hi", 20.5, True]
same_tuple = (1, 3, "Hi", 20.5, True)

print(sys.getsizeof(same_list),"bytes")  # 104 bytes
print(sys.getsizeof(same_tuple),"bytes") # 80 bytes

print(timeit.timeit(stmt="[1, 3, 'Hi', 20.5, True]", number=1000000)) # 0.022827666999546636
print(timeit.timeit(stmt="(1, 3, 'Hi', 20.5, True)", number=1000000)) # 0.003979875000368338





