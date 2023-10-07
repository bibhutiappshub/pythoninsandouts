# We can create expressions in a single line as well
name = "Bibhuti"; print(f"My name is {name}")
id = 1234
# Check types
print(type(name))
print(type(id))

# Checking the type using conditional statements
print(type(name) == str)
print(type(id) == int)
print(isinstance(name,str))
print(isinstance(id,float))

# Type Casting
float_val = float(2)
int_val = int(2.9)
str_int = int("20")
print(float_val)
print(int_val)
print(isinstance(str_int,int))

# Operators
height = 5
height +=5
print(height)
# Logical Operators
cond1 = True
cond2 = False

if cond1 or cond2:
    print("Either one of them is True")
else:
    print("Both the conditions are false")

if cond1 and cond2:
    print("Both are True")
else:
    print("Either one of them is False")

if not cond2:
    print("True")

# and/or expressions
# or expression checks if X is false then Y else X
# and expression checks if X is false then X else Y
print(0 or 1)
print(0 and 1)
print('hi' or 'hey')
print('hi' and 'hey')
print([] or False)
print([] and False)
# Ternary Operator
age = 18
is_adult = True if age >= 18 else False
print(is_adult)
