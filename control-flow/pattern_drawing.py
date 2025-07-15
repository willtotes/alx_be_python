
#print("*", end="")
pattern = int(input("Enter the size of the pattern: "))

i = 0
while i < pattern:
    j = 0
    while j < pattern:
        print("*", end="")
        j += 1
    print()
    i += 1
