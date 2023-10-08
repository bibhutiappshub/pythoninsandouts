# Set act like tuples but they are not ordered. Also they are mutable.

name1 = {"Bibhuti","Plaban","Soumya","Plaban"}
name2 = {"Ajit","Prasant","Soumya"}
name3 = {"Bibhuti","Plaban"}
print(name1)

# Find intersection
print(name1 & name2)

# Do union
print(name1 | name2)

# Do difference
print(name1 - name2)

# Check subset and superset
print(name1 > name3)
print(name3 < name1)

# Convert Sets to list
print(list(name1))