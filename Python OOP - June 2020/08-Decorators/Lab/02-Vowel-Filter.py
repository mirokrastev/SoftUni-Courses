def vowel_filter(function):
    VOWELS = {'a', 'e', 'i', 'o', 'u', 'y'}

    def wrapper():
        ll = function()
        return list(filter(lambda x: x.lower() in VOWELS, ll))

    return wrapper