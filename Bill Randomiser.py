import random
Amount_Of_People = int(input("How many people are there\n"))
Bill_Amount = float(input("How much is the bill:\nR"))
Names_Of_People = []
for i in range(Amount_Of_People):

    Names_Of_People.append(input(f"Person {i+1} name:\n"))


payer = random.choice(Names_Of_People)

print("The person paying the bill is:", payer , "\nYour total is R",Bill_Amount)


