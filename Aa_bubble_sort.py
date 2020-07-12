dict1 = {}
n = int(input("Enter number of items to be sorted: "))
for i in range(n):
    item = int(input(f"Enter item {i+1}: "))
    dict1[i] = item

print("Before sorting: ", list(dict1.values()))

l = len(dict1)
for x in range(l-1, 0, -1):
    for k in dict1.keys():
        if k == x:
            break
        if dict1[k+1] < dict1[k]:
            dict1[k], dict1[k+1] = dict1[k+1], dict1[k]

print("After sorting: ", list(dict1.values()))
