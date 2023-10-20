from collections import Counter
from collections import namedtuple
from collections import deque


a = "aaabbbbcccdddaccbb"
count_dict = Counter(a)
print(count_dict) # Provides each character count in a dictionary and sort it in decreasing order.
print(list(count_dict.items())) # List of tuples
print(list(count_dict.elements())) # Create a list of all the elements

# namedtuple create a class and attributes
Point = namedtuple("Point",'name,age')
pt = Point(name="Bibhuti",age=36)
print(pt.name," ", pt.age)

# double ended queue with both append/pop/extend operations allowed for both the sides.
d = deque()
d.append(1)
d.append(2)
d.appendleft(0)
d.pop()
d.popleft()
d.extend([3, 4, 5])
d.extendleft([-1, -2, -3])
print(d)
