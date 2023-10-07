# Empty List
my_empty_list = []
# List with simillar types
same_type_list = ["Hi","Hello","Namaskar","Adab","Sasriyakal"]
# Different type list
diff_type_list = [10,"Hi",25.35,True]
print(my_empty_list)
print(same_type_list)
print(diff_type_list)

# in operator to check the element existence
print("Hello" in same_type_list)
print("Bye" in same_type_list)

# Update item in the list
same_type_list[1] = "Bye"
print(same_type_list)
# Access elements through indexes
print(same_type_list[1])
print(same_type_list[-1])
# Slice/ substring of list
print(same_type_list[0:1])
print(same_type_list[:2]) #Start from 0 to before 2
print(len(same_type_list))

# Add items into the list i.e Appending to list
same_type_list.append("Ola")

# Add a new list into existing list
same_type_list.extend(["Hey",False,"Kem Chho"])
# ALternate way
same_type_list += ["kaisan ba"]
print(same_type_list)
# Remove items
same_type_list.remove("kaisan ba")
print(same_type_list)
print(same_type_list.pop())
print(same_type_list)
# Insert at a specific position
same_type_list.insert(3,"test_item")
print(same_type_list)
# Add multiple item into a list
same_type_list[1:2] = ["item1","item2"]
print((same_type_list))

# Sort lists
my_list = ["Hello","Hi","bye","Bingo"]
# Sorting modifies the list content. So avoid that we can copy the content first and then sort
cloned_list = my_list[:]
my_list.sort() # It sorts the upper case letter words first and then lower case. Solve that using below approach
print(my_list)
my_list.sort(key=str.upper)
print(my_list)
print(cloned_list)
# If we don't want the sort method to not modify the original list we can use global function sorted.
print(sorted(cloned_list,key=str.lower))
print(cloned_list)
