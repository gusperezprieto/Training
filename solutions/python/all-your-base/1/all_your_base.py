def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for num in digits:
        if not (0 <= num < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")

    decimal_value = 0

    response = []

    for index,value in enumerate(digits):
        decimal_value += value * (input_base ** (len(digits) - index - 1))

    exp = 0

    while output_base ** exp <= decimal_value:
        exp += 1

    exp -= 1

    while exp >= 0:
        response.append(decimal_value // (output_base ** exp))
        decimal_value %=  (output_base ** exp)
        exp -= 1

    if len(response) == 0:
        return [0]

    return response

    
        


