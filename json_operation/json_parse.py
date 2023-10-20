import json
from json import JSONEncoder
from json import JSONDecoder

person_dict = {"name": "Matt",
               "age": 35,
               "city": "Boston",
               "hasChildren": False,
               "titles": ["Engineer", "Programmer", "Architect"]
               }
print(person_dict)

# Convert python object into JSON string
person_json = json.dumps(person_dict, indent=4, sort_keys=True)
print(person_json)

# Dump it to file
with open('person.json', 'w') as file:
    json.dump(person_dict, file, indent=4)

#Convert from JSON string to python object
person_deserialized_obj = json.loads(person_json)  # Loads from string
print(person_deserialized_obj)

with open("person.json", "r") as file:
    persondictobj = json.load(file)

print(persondictobj)

def encode_user(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON Serializable')

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class UserEncoder(JSONEncoder):
    # Alternate way to make a class JSON serializable
    def default(self, obj):
        if isinstance(obj, User):
            return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}

        return JSONEncoder.default(self, obj)


class UserDecoder(JSONDecoder):
    # Alternate way to make a class JSON serializable
    def __init__(self):
        JSONDecoder.__init__(self, object_hook=UserDecoder.from_dict)

    @staticmethod
    def from_dict(dictobj):
        if User.__name__ in dictobj:
            return User(name=dictobj["name"], age=dictobj["age"])
        return dictobj

user1 = User('Matt', 37)
user2 = User('Nathan', 38)
user3 = User('Caesar', 39)
# userJson = json.dumps(user1) # This will throw Object of type User is not JSON serializable.
userJson1 = json.dumps(user1, default=encode_user)
userJson2 = json.dumps(user2, cls=UserEncoder)
userJson3 = UserEncoder().encode(user3)
print("User JSON1 : ", userJson1)
print("User JSON2 : ", userJson2)
print("User JSON3 : ", userJson3)

# Decode the object back
userobj1 = json.loads(userJson1)
userobj2 = json.loads(userJson2, cls=UserDecoder)
print(userobj1) # This will be a dictionary rather than User object
print(userobj2.name) # This will be a dictionary rather than User object
print(type(userobj2)) # This will be a dictionary rather than User object
