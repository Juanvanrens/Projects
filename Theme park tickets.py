Price = 0.0 # set price = 0
Height = float(input("What is your height in cm? ")) #user height
if Height < 120: #Height Check
    print("Sorry, your height is below 120cm, you may not purchase a ticket")
    exit(0)

Age = int(input("What is your age? ")) #age check
if 0 < Age < 10:
    print("You are too young to purchase a ticket")
    exit(0)

elif 10 <= Age < 12: #Price cat 1
    Price = float(99.99)

elif 12 <= Age < 18: #Price cat 2
    Price = float(99.99)

else:
    Price = float(149.99) #Price cat 3


Photo = input("Would you like a photo? (y/n)? ") #Photo upsell

if Photo == "y":
    Price += 29.99 #add photo price

print(f"Your price is R{Price}")

Receipt = input("Would you like to receipt? (y/n)? ") #ask for receipt

if Receipt == "y" or Receipt == "yes":
    print("Here is your receipt, enjoy the rest of your day!")


else:
        print("Enjoy the rest of your day!")

exit(0)


