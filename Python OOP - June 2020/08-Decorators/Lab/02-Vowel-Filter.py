def vowel_filter(function):
    def wrapper():
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return [i for i in function() if i in vowels]

    return wrapper