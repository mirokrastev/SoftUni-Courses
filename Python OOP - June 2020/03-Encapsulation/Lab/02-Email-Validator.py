class EmailValidator:
    import re
    pattern = r'([A-Za-z0-9\.]+)@([A-Za-z]+)\.([A-Za-z]+)'

    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return len(name) >= self.min_length

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def validate(self, email):
        reg = EmailValidator.re.match(EmailValidator.pattern, email)

        if not reg:
            return False

        name_var = self.__validate_name(reg.group(1))
        mail_var = self.__validate_mail(reg.group(2))
        domain_var = self.__validate_domain(reg.group(3))

        return all([name_var, mail_var, domain_var])