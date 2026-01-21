n = int(input('Enter a number n :'))

for i in range(1, 1+n):
    print(n, "X" ,i, "=", n*i )
    

n = int(input('Enter a number n :'))

for i in range(1, n+1):
    print(i, "Squared = ", i*i)
    
n = int(input('Enter a number n :'))
total = 0
for i in range(1, n+1):
    total += i
    
print("Sum of numbers from 1 to",n, "is", total)   

n = int(input('Enter a number n :'))
for i in range(1, 1+n):
    if i%2==0:
        print(i)    
        
n = int(input('Enter number n :'))
total = 0

for i in range(1, n+1):
    if i%2==0:
        total +=i
print("Sum of even numbers between 1 and",n,"is", total)       