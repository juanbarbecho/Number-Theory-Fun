#Juan Barbecho
#Euclidean Algorithm to find the GCD of two numbers
print("Give me two numbers and I will find their GCD")
A=a=int(input("What is the bigger number?"))
B=b=int(input("What is the smaller number?"))
r=1
count=0
while r!=0:
    print("GCD of",a,"and",b,"=")
    r=a%b
    a=b
    b=r
    count+=1
print("The GCD of",A,"and",B,"is",a)
print("The Algorithm repeated itself",count,"times to find the GCD")
    
