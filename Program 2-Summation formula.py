#Program 2- Proving a Summation Formula
#Juan Barbecho
#Tuesday, November 24th

print("This program shows that the sum of the perfect cubes equals (n^2(n+1)^2)/4")
print()

n=int(input("How many values of n do you want to sum?"))

sm=0

for i in range(1,n+1):
    sm += i**3

print()
print("The sum of the first",n,"terms equals",sm,)
print("The formula predicts a sum of",int(((n**2)*(n+1)**2)/4))

if sm == (n**2)*((n+1)**2)/4:
      print("The two values are equal! Therefore, the formula is true for n=",n)
else:
          print("The formula is not true for this value :(")
      
