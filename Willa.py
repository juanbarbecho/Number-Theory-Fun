#Finding Willa primes up to n


def primecheck(p):
    for i in range(3,int(p**0.5)+1):
        if (p%i)==0:
            return False
    return True
#confirms if a number is actually prime

#Finding Willas
count=0
n=int(input("How many numbers would you like to look at?"))
for p in range(2,n):
    if (2**(p-1)%p)==1:
        if primecheck(p):
            if(2**(p+10)-1)%(p+10)==1:
                print(p,"and",p+10,"are Willa primes!")
                count+=1
        else:
            print(p,"is almost prime...it's a pseudoprime")
print("I found",count,"pairs of Willa primes from 2 to",n)
