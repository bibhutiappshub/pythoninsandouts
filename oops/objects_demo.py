# Everything defined in Python is a object. We can access the methods on that ref variable.

age = 8 # Integers are immutable
print(id(age))
age = age+10 # Integers are immutable. so this creates a new object and assign the ref to age variable
print(id(age))
print(age.real) #Accessing integer class methods.
print(age.imag)