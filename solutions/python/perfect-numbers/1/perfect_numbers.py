def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    tot = 0
    for n in range(1,number//2+1):
        if number % n ==0:
            tot += n
    
    if tot == number:
        return "perfect"
    if tot < number:
        return "deficient"
    return "abundant"
