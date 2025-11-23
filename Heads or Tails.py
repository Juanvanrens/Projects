import random

Heads_Or_Tails = random.randint(1,2)


Heads_Or_Tails_Selection = str.casefold(input("Heads or tails? [H / T]"))

if (Heads_Or_Tails_Selection == "h" or Heads_Or_Tails_Selection == "heads") and Heads_Or_Tails == 1:

    print("Yay! You got Heads")

elif (Heads_Or_Tails_Selection == "t" or Heads_Or_Tails_Selection == "tails") and Heads_Or_Tails == 2:

    print("Yay! You got Tails")

elif (Heads_Or_Tails_Selection == "t" or Heads_Or_Tails_Selection == "tails") and Heads_Or_Tails == 1:

    print("Aww, You got Heads")

elif (Heads_Or_Tails_Selection == "h" or Heads_Or_Tails_Selection == "heads") and Heads_Or_Tails == 2:

    print("Aww, You got Tails")


else:
    print("You have not made a valid selection")
    exit(0)
