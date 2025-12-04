def commands(binary_str):

    actions = ["wink","double blink","close your eyes","jump"]

    response = []

    for index in range(4):
        if binary_str[4 - index] == "1":
            response.append(actions[index])

    if binary_str[0] == "1":
        response.reverse()

    return response
