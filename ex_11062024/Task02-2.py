# 2
# find factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print("Factorial of ",n," is ",fact)
