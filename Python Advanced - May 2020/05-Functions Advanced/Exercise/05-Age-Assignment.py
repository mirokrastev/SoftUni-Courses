def age_assignment(*args, **kwargs):
    d = {}
    abb = kwargs
    for i in args:
        d[i] = 0
    keys = d.keys()
    for i in abb:
        for key in keys:
            if i == key[0]:
                d[key] = abb[i]

    return d