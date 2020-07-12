# Tower 1 is source Tower
# Tower 2 is intermediate Tower
# Tower 3 is destination Tower


def toh(n, a, b, c):
    if n > 0:
        toh(n-1, a, c, b)
        print(f"Move a disc from tower {a} to {c}")
        toh(n-1, b, a, c)


n = int(input("Enter the number of discs: "))
print("The steps are: ")
toh(n, 1, 2, 3)
