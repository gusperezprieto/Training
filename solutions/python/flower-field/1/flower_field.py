def annotate(garden):
    # Function body starts here
    response = []
    
    y_len = len(garden)
    
    if y_len == 0:
        return garden
        
    x_len = len(garden[0])

    if x_len == 0:
        return garden

    for index_y in range(y_len):
        new_row = ""

        if len(garden[index_y]) != x_len:
            raise ValueError("The board is invalid with current input.")
            
        for index_x in range(x_len):
            if garden[index_y][index_x] == "*":
                new_row += "*"
            else:
                if garden[index_y][index_x] != " ":
                    raise ValueError("The board is invalid with current input.")
                    
                counter = 0
                # up left
                if index_y > 0 and index_x > 0 and garden[index_y-1][index_x-1] == "*":
                    counter +=1
                # up center
                if index_y > 0 and garden[index_y-1][index_x] == "*":
                    counter +=1
                # up right
                if index_y > 0 and index_x < x_len -1 and garden[index_y-1][index_x+1] == "*":
                    counter +=1
                # left
                if index_x > 0 and garden[index_y][index_x-1] == "*":
                    counter +=1
                # right
                if index_x < x_len - 1 and garden[index_y][index_x+1] == "*":
                    counter +=1
                # down left
                if index_y < y_len - 1 and index_x > 0 and garden[index_y+1][index_x-1] == "*":
                    counter +=1
                # down center
                if index_y < y_len - 1 and garden[index_y+1][index_x] == "*":
                    counter +=1
                # down right
                if index_y < y_len - 1 and index_x < x_len -1 and garden[index_y+1][index_x+1] == "*":
                    counter +=1

                if counter > 0: 
                    new_row += str(counter)
                else:
                     new_row += " "

        response.append(new_row)

    return response
                
                
            
            
