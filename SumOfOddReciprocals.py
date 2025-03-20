#Juan Barbecho
#The sum of the first n reciprocals of the odd numbers
#1/1 + 1/3 + 1/5 + 1/7 +...+ 1/n

print("This program will find the sum of the first n reciprocals of the odd numbers")
n=int(input("How many terms do you want to sum up?"))
sm=0
for i in range (1,n+1):
      if (i%2) != 0:
          sm += (1/i)
print("The sum of the first", n, "reciprocals of the odd numbers is equal to", sm)
