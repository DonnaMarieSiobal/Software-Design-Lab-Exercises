def product(m,n):
    if(m<n):
        return product(n,m)
    elif(n!=0):
         return(m+product(m,n-1))
    else:
         return 0


m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))

print("\nThe product of two positive integer is:", product(m, n))

