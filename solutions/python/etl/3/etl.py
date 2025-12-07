def transform(legacy_data):

    res = {}

    for key, letters in legacy_data.items():
        for letter in letters:
            res[letter.lower()] = key

    return res
