# Tuples are immutable.

names = ("Soumya","Bibhuti","Plaban")
# Accessing values from tuples
print(names[0])
print(names[-1])

# Get the index of particular item
print(names.index("Plaban"))
print(len(names))
print("Plaban" in names)
# names[0] = "Ajit" # This is not possible

# Get substring of tuple using slices
print(names[0:2])

#Sort tuples
print(sorted(names))
print(names)
# Add multiple items into the Tuples
new_tuple = names + ("Ajit","Prashant")
print(new_tuple)