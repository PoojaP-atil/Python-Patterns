#To get pattern 1 using *
for i in range(1,5,1):
    for j in range(1,i+1,1):
        print("*",end='')
    #End of inner loop
    print("")

# To get pattern 2
for i in range(1,5,1):
    #for space
    for k in range(1,(4-i)+1,1):
        print(" ",end='')
    for j in range(1,i+1,1):
        print("*",end='')
    #End of inner loop
    print("")

# To get pattern1 using numbers
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(i,end='')
    #End of inner loop
    print("")

# To get pattern 2 using numbers
for i in range(1,5,1):
    #for space
    for k in range(1,(4-i)+1,1):
        print(" ",end='')
    for j in range(1,i+1,1):
        print(i,end='')
    #End of inner loop
    print("")

#To get pattern 3
for i in range(1,5,1):
    #for space
    for k in range(1,(4-i)+1,1):
        print(" ",end='')
    for j in range(1,i+1,1):
        print("* ",end='')
    #End of inner loop
    print("")

# To get pattern 4
a=1
for i in range(1,5,1):
    for j in range(1,i+1,1):
        print(a,end=' ')
        i=i+1
        a=a+1
    #End of inner loop
    print("")

#To get pattern 5
a = 5
for i in range(1,a + 1,1):
    for j in range(1,a - i + 1,1):
        print("  ", end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i + 1,1):
        print(j, end=" ")
    print("")

# To get pattern 6
a = 4

for i in range(1, a + 1, 1):
    for j in range(a, i, -1):
        print(" ", end=" ")
    for j in range(1, i + 1, 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print("\n")

# new pattern
for i in range(1,6,1):
    for j in range(0,i,1):
        print(j+1,end='')
    #End of inner loop
    print("")


print("\n")

n = 5  # Number of rows
for i in range(1, n+1):
    # Print spaces
    for j in range(n, i, -1):
        print(" ", end="")
    # Print numbers in decreasing order
    for k in range(i, 0, -1):
        print(k, end="")
    print("\r")

#To get inverse of pattern 1 using *
for i in range(4,0,-1):
    for j in range(1,i+1,1):
        print("*",end='')
    #End of inner loop
    print("")
print("\n")

# To get inverse of pattern 2
for i in range(4,0,-1):
    #for space
    for k in range(1,(3-i)+2,1):
        print(" ",end='')
    for j in range(1,i+1,1):
        print("*",end='')
    #End of inner loop
    print("")
print("\n")

#To get inverse of pattern 3
for i in range(4,0,-1):
    #for space
    for k in range(1,(4-i)+1,1):
        print(" ",end='')
    for j in range(1,i+1,1):
        print("* ",end='')
    #End of inner loop
    print("")