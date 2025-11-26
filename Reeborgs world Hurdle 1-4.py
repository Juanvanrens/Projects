#Solution to Reeborgs World Hurdle 1-4


def turn_right():
    for i in range(3):
        turn_left()


while at_goal() == False:
    if wall_in_front():
        turn_left()
    elif wall_in_front() and not is_facing_north():
        turn_right()
        move()
        turn_right()

    while at_goal() == False and wall_in_front() == False and wall_on_right():
        move()

    while is_facing_north() and wall_on_right() == False:
        turn_right()
        move()
        turn_right()
    while wall_on_right() == False and front_is_clear():
        move()



