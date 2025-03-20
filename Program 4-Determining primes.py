#Juan Barbecho
#Algorithm that determines if a number is prime

n = int(input("Enter a positive integer:"))

prime = "yes"

summ = 1+n
num = 2

print("1 and",n,"are factors of",n)

for i in range (2,int(n**0.5)+1):
    if (n%i)==0:
        if(i==int(n/i)):
            print(i,"is a factor of",n)
            num+=1
            summ+=i
        if(i!=int(n/i)):
            print(i,"and",int(n/i),"are factors of",n)
            summ+=i+int(n/i)
            num+= 2
        prime="no"
if prime == "no":
    print(n,"is not prime")
if prime == "yes":
    print("Turns out",n,"is prime!YAY!")
print("The sum of the divisors is",summ)
print(n,"has",num,"divisors")
