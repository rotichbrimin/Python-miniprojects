
# nationality = 'Kenya'
voted_count = 0
total_people = 0
minors = 0
while True:
    nationality = input("Enter your nationality :").lower()
    age = int(input("Enter your age: "))
    
    if age < 0:
        print("Age cannot be negative. Please enter a valid age.")
        continue
    if age >= 18 and nationality == 'kenya': 
        print("You are kenyan adult and can vote")
        voted_count += 1
        total_people += 1
    elif age < 18 and nationality == 'kenya':
        print("You are a Kenyan minor and cannot vote!")
        total_people += 1
        minors += 1
    elif age >= 18 and nationality != 'kenya':
        print("Sorry! You are not a Kenyan and cannot vote !")
        total_people += 1
    else:
        print("Sorry! You are not a Kenyan and a minor, so you cannot vote !")
        total_people += 1
        minors += 1

    next_person = input("Is there another person to check? (yes/no): ").lower()
    if next_person != 'yes':
        break

print(f"Total number of people checked are {total_people}")
print(f"Total number of people who voted are {voted_count}")  
print(f"Total number of minors are {minors}") 