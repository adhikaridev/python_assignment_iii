dict1 = {}
n = int(input("Enter number of items to be sorted: "))
for i in range(n):
    item = int(input(f"Enter item {i+1}: "))
    dict1[i] = item
# dict1 = {0: 46, 1: 14, 2: 43, 3: 27, 4: 70, 5: 41, 6: 45, 7: 21, 8: 57}
print("Before sorting: ", list(dict1.values()))
l = len(dict1)
for i in range(1, l):
    value = dict1[i]
    j = i - 1
    while j>=0 and value < dict1[j]:
        dict1[j+1] = dict1[j]
        j = j - 1
    dict1[j+1] = value
print("After sorting: ", list(dict1.values()))
