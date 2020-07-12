def interpolation_search(seq, search_item, length):
    l = 0
    h = length - 1
    while l <= h and search_item >= seq[l] and search_item <= seq[h]:
        if l == h:
            if seq[l] == x:
                return l;
            return -1
        pos = l + int(((float(h-l) / (seq[h] - seq[l])) * (search_item - seq[l])))
        if seq[pos] == search_item:
            return pos
        if seq[pos] < search_item:
            l = pos + 1
        else:
            h = pos - 1
    return -1



n = int(input("Enter the number of items in the list: "))
print("Enter integer items in ascending order: ")
seq = []
for x in range(n):
    item = int(input())
    seq.append(item)
print("Entered list: ", seq)
search_item = int(input("Enter integer item to be searched: "))
length = len(seq)
search_item_index = interpolation_search(seq, search_item, length)
if search_item_index == -1:
    print("Item not found.")
else:
    print(f"Item found. Index is {search_item_index}")
