#Verifying the Hockey Stick Identity

#factorial and combination functions

def factorial (m) :
    p = 1
    for i in range (1,m+1):
        p *= i
    return (p)
        
def combination (n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

n = int(input("Enter a positive integer n:"))

k = int(input("Enter another positive integer k, k<=n"))


#Adds up kCk + k+1Ck + k+2Ck + ... + nCk

sm = 0
for i in range (k,n+1):
    sm += combination(i,k)

#Tells if it works or not

if sm == combination((n+1),(k+1)):
    print("The Hockey Stick Identity holds true! :)")
else:
    print(":( The Hockey Stick Identity doesn't work")
    
print(combination((n+1),(k+1)),"= n+1Ck+1")

print(sm,"= kCk + k+1Ck + k+2Ck + ... + nCk")

if sm == combination((n+1),(k+1)):
    print ("The two values are equal!")

                     
