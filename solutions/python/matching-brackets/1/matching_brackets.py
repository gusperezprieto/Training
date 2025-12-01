def is_paired(input_string):

    stack = []
    
    for character in input_string:
        if character not in "[]{}()":
            continue
        if character in "{[(":
            stack.append(character)

        if character in "}])" and len(stack) == 0:
            return False

        if (character == "}" and stack.pop() != "{") or (character == ")" and stack.pop() != "(") or (character == "]" and stack.pop() != "["):
            return False
            
    return len(stack) == 0
           
        
