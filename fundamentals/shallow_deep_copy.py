# Shallow and deep copy only make sense in case of mutable objects
# Shallow copy : One level deep, only references of nested child objects
# Deep copy : full independent copy

import copy

#Different ways of shallow copies
org_list = [1, 2, 3, 4]
cpy1 = org_list.copy()
cpy2 = list(org_list)
cpy3 = org_list[:]
cpy4 = copy.copy(org_list)

# Multiple level copies
org = [[1, 2, 3, 4],[5, 6, 7, 8]]
cpy = org
cpy[0][1] = 0
print(cpy)
print(org)

# Deep copy
orglist = [[1, 2, 3, 4],[5, 6, 7, 8]]
cpy = copy.deepcopy(orglist)
cpy[0][1] = 0
print(cpy)
print(orglist)