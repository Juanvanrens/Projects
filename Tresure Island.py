print(r'''
$$\       $$\  $$$$$$\                  $$$$$$\  $$\                         $$\            $$|
$$ |      \__|$$  __$$\                $$  __$$\ \__|                        $$ |           $$ |
$$ |      $$\ $$ /  \__|$$$$$$\        $$ /  \__|$$\ $$$$$$\$$$$\  $$\   $$\ $$ | $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$  
$$ |      $$ |$$$$\    $$  __$$\       \$$$$$$\  $$ |$$  _$$  _$$\ $$ |  $$ |$$ | \____$$\_$$  _|  $$  __$$\ $$  __$$  |
$$ |      $$ |$$  _|   $$$$$$$$ |       \____$$\ $$ |$$ / $$ / $$ |$$ |  $$ |$$ | $$$$$$$ | $$ |    $$ /  $$ |$$ |  \__|
$$ |      $$ |$$ |     $$   ____|      $$\   $$ |$$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$  __$$ | $$ |$$\ $$ |  $$ |$$ |
$$$$$$$$\ $$ |$$ |     \$$$$$$$\       \$$$$$$  |$$ |$$ | $$ | $$ |\$$$$$$  |$$ |\$$$$$$$ | \$$$$  |\$$$$$$  |$$ |
\________|\__|\__|      \_______|       \______/ \__|\__| \__| \__| \______/ \__| \_______|  \____/  \______/ \__|
''')

gender = str.casefold(input("Welcome to the life simulator!\nAre you a boy or a girl? [boy / girl]\n\n"))
if gender == "boy":
    print("After High school university decisions are coming up, do you choose to go or stay unemployed?")
    employment = str.casefold(input("Would you like to go or stay unemployed? [University / Unemployed]\n"))

    if employment == "university":
        drink = str.casefold(input("Do you put effort into your studies or do you drink everyday? [Study or drink]\n"))

        if drink == "drink":
            print("\nYou eventually become an alcoholic and drop out.\nYou beat your wife and kids and you're a terrible person.\nYou eventually die from liver failure.\nGame Over. Do better")
            exit(0)
        elif drink == "study":
            print("\nYou study hard and become an engineer. Well done")
            exit(0)

        else:
            print("\nYou have not made a valid selection")
            exit(0)

    elif employment == "unemployed":
        job = str.casefold(input("Do you try hard to find a job or are you a couch potato [Job / Couch potato]\n"))
        if job == "job":
            print("\nYou work hard, build experience and find a job.\nYou are a mechanic\nWell done Frikkie.")
            exit(0)

        elif job == "couch potato":
            print("\nYou overeat, loose all ambition for life and die on your piss soaked sheets.\nWomp womp bitch")
            exit(0)

        else:
            print("\nYou have not made a valid selection")



    else:
        print("\nYou have not made a valid selection")
        exit(0)


elif gender == "girl":

    employment = str.casefold(input("Would you like to go or stay unemployed? [University / Unemployed]\n"))

    if employment == "university":
        study = str.casefold(input("Do you put effort into your studies or do you go shopping everyday? [Study or Shop]\n"))

        if study == "shop":
            print(  "\nYou max out your credit cards buying shoes and bags.\nYour apartment is full of boxes you never open.\nYou lie to friends and family about your spending.\nDebt collectors start calling and your financial life crumbles.\nYou eventually lose your apartment and end up on the streets.\nGame Over. Do better" )
            exit(0)
        elif study == "study":
            print("\nYou study hard and become an doctor. \nWell done Susan")
            exit(0)

        else:
            print("\nYou have not made a valid selection")
            exit(0)

    elif employment == "unemployed":
        job = str.casefold(input("Do you try hard to find a job or are you an unemployed diva [Job / Unemployed diva]\n"))
        if job == "job":
            print("\nYou work hard, build experience and find a job.\nYou are a mechanic\nWell done Frikkie.")
            exit(0)

        elif job == "unemployed diva":
            print("\nYou get pregnant and act like everything’s fine, but you’re just spiraling.\nYou overeat, ignore your responsibilities, and let your place turn into a garbage pit.\nYou lie to everyone, including yourself, as your life slowly unravels.\nEventually everything collapses and you’re left alone in the chaos you made.\nWomp womp, you really fucked up.")
            exit(0)

        else:
            print("\nYou have not made a valid selection")



    else:
        print("\nYou have not made a valid selection")
        exit(0)


