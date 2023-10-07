from enum import Enum


# It's the only way we declare CONSTANTS in python. It's through Enums.
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State["ACTIVE"].value)
print(State["INACTIVE"].value)
print(State.ACTIVE.value)
print(State.INACTIVE.value)
# Listing all ENUM values
print(list(State))
print(type(State))