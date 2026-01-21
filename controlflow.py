# Write code below 💖


height = int(input('Enter your height in CM :'))
credits = int(input('Enter your credits :'))

if height >=137 and credits>=10:
  print('Enjoy your ride!')
elif credits>=10 and height<137:
  print('You are not tall enough to ride!')
elif height>=137 and credits<10:
  print('You do not have enough credits!')
else:
  print('You do not meet the requirements!')
