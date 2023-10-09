# Every Python file acts as a module. We can import whole file or specific function in
# other file to use it.
import libraries
from libraries import call
call()
libraries.show()

# We can also import python libraries from other python packages. But the catch is
# it should contain __init__.py file inside it.

from lib import py_library

# To include specific functions
from lib.py_library import hello

py_library.hi()
hello()
