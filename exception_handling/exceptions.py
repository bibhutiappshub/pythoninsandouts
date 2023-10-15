try:
    result = 2 / 0
except ZeroDivisionError:
    print("You can't divide any number by 0!!!")
else:
    print("This will execute if there is no error!!!")
finally:
    print("This will execute whether we have error or not!!!")