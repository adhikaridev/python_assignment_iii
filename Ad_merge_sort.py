def merge_sort(list1):
    length = len(list1)
    if length > 1:
        mid = int(len(list1) / 2)
        left = list1[:mid]
        right = list1[mid:]
        merge_sort(left)
        merge_sort(right)
        a, b, c = 0, 0, 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list1[c] = left[a]
                a = a + 1
            else:
                list1[c] = right[b]
                b = b + 1
            c = c + 1
        while a < len(left):
            list1[c] = left[a]
            a = a + 1
            c = c + 1
        while b < len(right):
            list1[c] = right[b]
            b = b + 1
            c = c + 1




list1 = []
n = int(input("Enter number of items to be sorted: "))
for i in range(n):
    item = int(input(f"Enter item {i+1}: "))
    list1.append(item)
print ("Before Sorting: ", list1)
merge_sort(list1)
print("After Sorting: ", list1)
