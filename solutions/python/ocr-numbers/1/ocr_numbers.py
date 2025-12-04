def convert(input_grid):

    print(input_grid)

    def get_number(line1, line2, line3, line4):

        firt_line   = [" _ ", "   ", " _ ", " _ ", "   ", " _ ", " _ ", " _ ", " _ ", " _ "]
        second_line = ["| |", "  |", " _|", " _|", "|_|", "|_ ", "|_ ", "  |", "|_|", "|_|"]
        third_line =  ["|_|", "  |", "|_ ", " _|", "  |", " _|", "|_|", "  |", "|_|", " _|"]

        for index in range(10):
            if line1 == firt_line[index] and line2 == second_line[index] and line3 == third_line[index] and line4 == "   ":
                return str(index)

        return "?"

    response = []

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    for index in range(0, len(input_grid), 4):
        
        if len(input_grid[index]) % 3 != 0 or len(input_grid[index+1]) % 3 != 0 or len(input_grid[index+2]) % 3 != 0 or len(input_grid[index+3]) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

        translation = ""
        
        for index_row in range(0, len(input_grid[index]), 3):
            print("index_row " + str(index_row))
            translation += get_number(input_grid[index][index_row:index_row+3], 
                                     input_grid[index+1][index_row:index_row+3],
                                     input_grid[index+2][index_row:index_row+3],
                                     input_grid[index+3][index_row:index_row+3])

        response.append(translation)
            

    return ",".join(response)

