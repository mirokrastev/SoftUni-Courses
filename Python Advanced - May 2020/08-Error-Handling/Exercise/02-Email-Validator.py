class NameTooShortError(Exception):
    """
    raises exception nameTooShortError
    if the name in the email is less than or equal to 4 characters.
    """
    pass


class MustContainAtSymbolError(Exception):
    """
    raises exception MustContainAtSymbolError
    when there is no '@' in the email.
    """
    pass


class InvalidDomainError(Exception):
    """
    raises exception InvalidDomainError
    when the domain is invalid.
    """
    pass

def validate_name(name):
    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

def validate_symbol(arg):
    if '@' not in arg:
        raise MustContainAtSymbolError('Email must contain @')

def validate_domain(domain):
    domains = {'.com', '.bg', '.org', 'net'}

    if domain not in domains:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(domains)}')

import re
pattern = r'([A-Za-z]+)@[a-z]+(\.[a-z]+)'

while True:
    arg = input()
    reg = re.match(pattern, arg)

    validate_symbol(arg)

    name = reg.group(1)
    domain = reg.group(2)

    validate_name(name)
    validate_domain(domain)