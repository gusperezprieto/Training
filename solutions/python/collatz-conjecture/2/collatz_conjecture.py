def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    counter = 0

    while number > 1:
        counter += 1
        number = number * 3 + 1 if number % 2 else number//2

    return counter
