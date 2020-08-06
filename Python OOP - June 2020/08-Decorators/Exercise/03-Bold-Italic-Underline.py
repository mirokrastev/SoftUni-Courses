import re
opening_tag_p = r'<[a-z]>'
closing_tag_p = r'<\/[a-z]>'
full_pattern = r'<\/?[a-z]>'


def make_tags(string, opening, closing):
    opening_tags = re.findall(opening_tag_p, string)
    closing_tags = re.findall(closing_tag_p, string)
    raw_string = "".join(re.split(full_pattern, string))
    opening_tags.insert(0, opening)
    closing_tags.append(closing)

    return "".join(opening_tags) + "".join(raw_string) + "".join(closing_tags)


def make_bold(func):
    def wrapper(*args):
        string = func(*args)
        opening, closing = r'<b>', r'</b>'
        return make_tags(string, opening, closing)

    return wrapper


def make_italic(func):
    def wrapper(*args):
        string = func(*args)
        opening, closing = r'<i>', r'</i>'
        return make_tags(string, opening, closing)
    return wrapper


def make_underline(func):
    def wrapper(*args):
        string = func(*args)
        opening, closing = r'<u>', r'</u>'
        return make_tags(string, opening, closing)
    return wrapper