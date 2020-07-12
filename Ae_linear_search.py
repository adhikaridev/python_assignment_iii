# dict1 = {0: 46, 1: 14, 2: 43, 3: 27, 4: 70, 5: 41, 6: 45, 7: 21, 8: 57}
dict1 = {}
n = int(input("Enter number of items in the dictionary: "))
for i in range(n):
    item = int(input(f"Enter item {i+1}: "))
    dict1[i] = item
element = int(input("Enter an integer element to be searched: "))

f = 0
for key, value in dict1.items():
    if value == element:
        print(f"Element found. Index is {key}")
        f = 1
        break
if not f:
    print("Item not found.")
