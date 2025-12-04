def egg_count(display_value):
    counter = 0

    while display_value > 0:
        if display_value % 2 != 0:
            counter += 1
        display_value //= 2

    return counter
