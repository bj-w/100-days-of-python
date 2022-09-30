#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Tip calculator")
bill = float(input("What was the total bill?\n"))
percent = input("How much tip would you like to give? 10, 12, or 15?\n")
people = float(input("How many people are splitting?\n"))
tip = round((bill / people) * float("1." + percent), 2)

print(f"Each person should pay: ${tip}")