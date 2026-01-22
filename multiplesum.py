n=int(input('Enter a number :'))
total = 0

for i in range(1, n + 1):
    if i%3==0 or i%5==0:
        total +=i      
print('Sum of numbers divisible by 3 or 5 is ', total)