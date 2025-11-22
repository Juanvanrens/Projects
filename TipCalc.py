#Tip Calc


print("Hey, welcome to the tip calculator")
amount  = float(input("What did the bill come to? "))
perc = int(input("what % would you like to tip"))
people = int(input("How many people are splitting the bill? "))
total = amount * perc/100 + amount

print(f"The total will be: R {round(total,2)}")

totalpp = total/people

print(f"The total per person will be: R {round(totalpp,2)}")



