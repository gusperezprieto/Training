def square(number):
    if number < 1 or number > 64:
       raise ValueError("square must be between 1 and 64")
       return
        
    return 2**(number-1)



def total():

    tot = 0
    for index in range(1,65):
        tot += square(index)
    return tot
    
