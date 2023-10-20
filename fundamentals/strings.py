from timeit import default_timer as timer

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

my_sentence = "Hello Hi Bye"
words = my_sentence.split(" ")
print(words)
converted_str = " ".join(words)
print(converted_str)
# Performance comparison of joining a string.
my_rep_str = ['a'] * 1000000
joined_str1 = ""

begin = timer()
# bad approach for joining string because it will create a new string every time as string is immutable.
for i in my_rep_str:
    joined_str1 += i
end = timer()
print(f"Elapsed Time: {end-begin}") #Elapsed Time: 8.059475417000158

start = timer()
# more advanaced/cleaner/optmized approach
joined_str2 = ''.join(my_rep_str)
stop = timer()
print(f"Elapsed Time: {stop-start}") #Elapsed Time: 0.003793625000071188