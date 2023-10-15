try:
    result = 2 / 0
except ZeroDivisionError:
    print("You can't divide any number by 0!!!")
else:
    print("This will execute if there is no error!!!")
finally:
    print("This will execute whether we have error or not!!!")

# We can raise exceptions from a part of code using raise
try:
    raise Exception("This is an exception!!!")
except Exception as errormessage:
    print(errormessage)

# Userdefined Exception Class


class CustomException(Exception):
    pass


try:
    raise CustomException("This is a userdefined exception demo!!!")
except CustomException as errormessage:
    print(errormessage)


