#BMI Calculator


Weight = float(input("What is your weight in kg? "))
if 0 < Weight < 40 or Weight > 250  :
    print("You have not entered a valid weight, please try again")
    exit(0)

Heightinp = float(input("What is your height in cm? "))
Height = Heightinp/100

if 0 < Height < 1 or Height > 2.5 :
    print("You have not entered a valid height, please try again")
    exit(0)

BMI = Weight/(Height**2)


print("Your BMI is", round(BMI,2))

if 0 < BMI < 18.5:
    print("You are underweight")

elif 18.5 <= BMI < 25:
    print("You are normal weight")

elif 25 > BMI < 30:
    print("You are over weight")

else:
    print("You are obese")