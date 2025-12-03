def answer(question):

    def is_number(word):
        if len(word) > 0 and ((word[0] == "-" and word[1:].isdigit()) or (word[0].isdigit())):
            return True
        return False


    question = question.replace("What is", "Whatis").replace("multiplied by","multipliedby").replace("divided by","dividedby").rstrip(question[-1])

    words = question.split()

    if len(words) < 2 or words[0] != "Whatis":
        raise ValueError("syntax error")

    if not is_number(words[1]):
        raise ValueError("syntax error")
    tot = int(words[1])
   
    for index in range(2, len(words), 2):

        if is_number(words[index]):
            raise ValueError("syntax error")
        if words[index] not in ("plus","minus","multipliedby","dividedby"):
            raise ValueError("unknown operation")
        if index == len(words) - 1 or not is_number(words[index + 1]):
            raise ValueError("syntax error")
        
        if words[index] == "plus":
            tot += int(words[index + 1])
        elif words[index] == "minus":
            tot -= int(words[index + 1])
        elif words[index] == "multipliedby":
            tot *= int(words[index + 1])
        elif words[index] == "dividedby":
            tot //= int(words[index + 1])
        else:
            raise ValueError("syntax error")
     
    return tot