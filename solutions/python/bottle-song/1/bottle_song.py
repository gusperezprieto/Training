def recite(start, take=1):
    response = []
    numbers = ["no","One","Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

    for index in range(start, start-take, -1):
        response.append(f"{numbers[index]} green bottle{'s' if index > 1 else ''} hanging on the wall,")
        response.append(f"{numbers[index]} green bottle{'s' if index > 1 else ''} hanging on the wall,")
        response.append("And if one green bottle should accidentally fall,")
        response.append(f"There'll be {numbers[index-1].lower()} green bottle{'s' if index-1 != 1 else ''} hanging on the wall.")
        if index > start-take+1:
            response.append("")
                        
    return response
