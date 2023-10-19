# Key-Value pairs, Unordered, Mutable
mydict = {"name":"Bibhuti", "age":36, "city":"New York"}
print(mydict)

# We can use dict builtin function to create dictionary
my_new_dict = dict(name="Plaban", age=36, city="Panaspada")
# Length of the dictionary
print(len(mydict))
print(my_new_dict)

# We can use tuple as key as well because it is immutable but not list
mytuple = ("Bibhuti", 35)
newdict = {mytuple:25}
print(newdict)

# We can change items of a dictionary as it is mutable
mydict["name"] = "Soumya"
print(mydict)

# Delete items from dictionary
# del mydict["name"]  # Delete name key value pair
# mydict.pop("name")  # Removes name key value pair
# mydict.popitem() # Removes the last key value pair of the dictionary

# Check a key present inside a dictionary
if "age" in mydict:
    print("age key exists inside dictionary")

# Loop through dictionary
for key in mydict:
    print("Key:", key, "Value:", mydict[key])

for key in mydict.keys():
    print("Key:", key, "Value:", mydict[key])

for value in mydict.values():
    print("Value:", value)

# Copying dictionaries
copied_dict = mydict # If we change anything in copied dict then will reflect in the original one.
act_copy = mydict.copy()
act_copy["email"] = "soumya@gmail.com"
print(mydict)
print(act_copy)

# Update existing dictionaries key
mydict.update(my_new_dict)
print(mydict)

