# Simple declaration
my_str = "Hello"
str_with_quote = 'Hi'

# Multiline String
multi_line_str = """
Hi,
This is a

multiline string
"""
print(multi_line_str)

# Common methods
name = "Bibhuti"
print(name) # Bibhuti
print(name.lower())  #return bibhuti. It returns a new string rather than changing the original one
print(name.upper())
print(len(name))
print('Bi' in name) # Check substring

# Escape characters
my_str = "He\"lo"
my_quoted_str = 'He"l\'o'
escape_chars = 'He\nlo'
print(my_str)
print(my_quoted_str)
print(escape_chars)
print(my_quoted_str.strip())

# Accessing characters from a string
print(name[1]) # From left to right indexing starts with 0
print(name[-1]) # If negative index it returns the character of mentioned position from right

# Slicing or getting substring
print(name[1:3]) # Get characters starting from 1 and ending before 3

# Boolean checking
int_val=0 # Zero or blank string or empty datastructures are False.
empty_str = ""
bool_val = True
if int_val == False:
    print("True")

if not int_val:
    print("True")

print(type(bool_val) == bool)