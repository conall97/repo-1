
#n = int(input("Enter number of rows: "))
n = 5

print("Pattern 1")
for i in range(1, n+1):
    print("* "*i)
print()

print("Pattern 2")
for i in range(n, 0, -1):
    print("$ "*i)
print()

print("Pattern 3")
for i in range(1, n+1):
    print("  "*(n-i) + "# "*i)
print()

print("Pattern 4")
for i in range(n, 0, -1):
    print("  "*(n-i) + "% "*i)
print()

print("Pattern 5")
for i in range(1, n+1):
    print(" "*(n-i) + "£ "*i)
print()

print("Pattern 6")
for i in range(1, n+1):
    print(" "*(n-i) + "^ "*i)
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "^ "*i)
print()
