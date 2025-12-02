def score(x, y):

    square_hypotenuse =  x**2 + y**2

    if square_hypotenuse <= 1:
        return 10
    if square_hypotenuse <= 25: 
        return 5
    if square_hypotenuse <= 100: 
        return 1
        
    return 0
    
