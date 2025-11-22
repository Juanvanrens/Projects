Price = 0.00

Small = 59.99
Medium = 99.99
Large = 149.99

Pepperoni_Small = 13.99
Pepperoni_Medium_Large = 18.99
Cheese_Price = 9.99

print("Welcome to Python Pizza!")

Order = input("Would you like a Small, Medium or Large Pizza? ")
if Order == "Small":
    Price += Small
    Pepperoni = input("Would you like to add Pepperoni? ")
    if Pepperoni == "Yes":
        Price += Pepperoni_Small

    elif Pepperoni == "No":
        Price = Price

    else:
        print("You have entered an invalid option. Please try again.")

    Cheese = input("Would you like to add Cheese? ")
    if Cheese == "Yes":
        Price += Cheese_Price
        print(f"Your total comes to: R{Price}\nThank you for shopping with us")
    elif Cheese == "No":
        Price = Price
        print(f"Your total comes to: R{Price}\nThank you for shopping with us")

    else:
        print("You have entered an invalid option. Please try again.")

elif Order == "Medium":
    Price += Medium
    Pepperoni = input("Would you like to add Pepperoni? ")
    if Pepperoni == "Yes":
        Price += Pepperoni_Medium_Large

    elif Pepperoni == "No":
        Price = Price

    else:
        print("You have entered an invalid option. Please try again.")

    Cheese = input("Would you like to add Cheese? ")
    if Cheese == "Yes":
        Price += Cheese_Price
        print(f"Your total comes to: R{Price}\nThank you for shopping with us")

    elif Cheese == "No":
        Price = Price
        print(f"Your total comes to: R{Price}\nThank you for shopping with us")

    else:
        print("You have entered an invalid option. Please try again.")

elif Order == "Large":
    Price += Large
    Pepperoni = input("Would you like to add Pepperoni? ")
    if Pepperoni == "Yes":
        Price += Pepperoni_Medium_Large

    elif Pepperoni == "No":
        Price = Price

    else:
        print("You have entered an invalid option. Please try again.")

    Cheese = input("Would you like to add Cheese? ")
    if Cheese == "Yes":
        Price += Cheese_Price
        print(f"Your total comes to: R{Price}\nThank you for shopping with us")

    elif Cheese == "No":
        Price = Price
        print(f"Your total comes to: R{Price}\nThank you for shopping with us")

    else:
        print("You have entered an invalid option. Please try again.")

else:
    print("You have entered an invalid option. Please try again.")


