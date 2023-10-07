employee = {"id":1234,"name":"Bibhuti",8:10}
print(employee[8])
print(employee["name"])
print(employee.get("id"))

# Modifying dictionary contents
employee[8] = 50
print(employee)

# Get default value if key is not present in the dictionary
print(employee.get("age",37))
print(employee.pop(8)) #It removes the specified key from dictionay and returns the value of the popped key
print(employee)
print(employee.popitem()) #It removes the last key value pair from dictionay and returns the key value pair of the popped key
print(employee)
print("id" in employee) # Chek key existence inside the dictionary

# Get all the keys list
print(list(employee.keys()))
print(list(employee.values()))
print(list(employee.items()))

# Add new key value pair to dictionary
employee["age"] = 37
print(employee)

# Clone/copy a dictionary
employee_copy = employee.copy()
print(employee_copy)