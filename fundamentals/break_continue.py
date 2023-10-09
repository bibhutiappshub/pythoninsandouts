my_list = [1,2,3,4]

# break will break the loop where continue skip that iteration and continue to the next one.

for item in my_list:
    if item == 2:
        continue
    print(item)

print("=====")

for item in my_list:
    if item == 2:
        break
    print(item)