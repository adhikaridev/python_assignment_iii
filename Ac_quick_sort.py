def partition(dict1, l, h):
    i = l - 1
    pivot = dict1[h]
    for j in range(l, h):
        if dict1[j] <= pivot:
            i += 1
            dict1[i], dict1[j] = dict1[j], dict1[i]
    dict1[i+1], dict1[h] = dict1[h], dict1[i+1]
    return i+1


def quick_sort(dict1, l, h):
    if l < h:
        pi = partition(dict1, l, h)
        quick_sort(dict1, l, pi-1)
        quick_sort(dict1, pi+1, h)


dict1 = {}
n = int(input("Enter number of items to be sorted: "))
for i in range(n):
    item = int(input(f"Enter item {i+1}: "))
    dict1[i] = item
# dict1 = {0: 46, 1: 14, 2: 43, 3: 27, 4: 70, 5: 41, 6: 45, 7: 21, 8: 57}
print("Before sorting: ", list(dict1.values()))
length = len(dict1)
quick_sort(dict1, 0, length-1)
print("After sorting: ", list(dict1.values()))
