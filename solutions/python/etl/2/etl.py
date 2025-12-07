def transform(legacy_data):

    res = {}

    for key in legacy_data:
        for letter in legacy_data[key]:
            res[letter.lower()] = key

    return res
