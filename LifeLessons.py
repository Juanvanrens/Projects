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

print("Welcome to the life simulator!\nLet's see where your choices take you.")
employment = str.casefold(input("After high school, do you pursue further education or start working? [University / Work]\n"))

if employment == "university":
    effort = str.casefold(input("Do you put effort into your studies or slack off? [Study / Slack]\n"))

    if effort == "slack":
        print("\nYou struggle to keep up with your courses and eventually drop out.\nYou face setbacks but can try again in the future.\nGame Over. Reflect and try a better path next time.")
        exit(0)
    elif effort == "study":
        print("\nYou focus and excel in your studies, building a solid foundation for your career.\nWell done!")
        exit(0)
    else:
        print("\nInvalid selection. Try again.")
        exit(0)

elif employment == "work":
    diligence = str.casefold(input("Do you actively seek to grow your skills or coast along? [Work Hard / Coast]\n"))

    if diligence == "work hard":
        print("\nYou work diligently, gain experience, and build a fulfilling career.\nWell done!")
        exit(0)
    elif diligence == "coast":
        print("\nYou drift through jobs without learning new skills, making life more challenging.\nGame Over. Time to rethink your approach.")
        exit(0)
    else:
        print("\nInvalid selection. Try again.")
        exit(0)

else:
    print("\nInvalid selection. Try again.")
    exit(0)