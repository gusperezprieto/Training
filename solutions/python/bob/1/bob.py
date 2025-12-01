def response(hey_bob):
    is_upper = hey_bob.isupper()
    is_question = hey_bob.strip().endswith("?")
    is_silence =hey_bob.isspace() or len(hey_bob) == 0

    if is_upper and is_question:
        return "Calm down, I know what I'm doing!"
    if is_upper:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    if is_silence:
        return "Fine. Be that way!"

    return "Whatever."
