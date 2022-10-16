class PhoneException(Exception):
    pass

class FormatError(PhoneException):
    pass

class AmountError(PhoneException):
    pass

class CountryCodeError(PhoneException):
    pass

class ProviderError(PhoneException):
    pass


def check_number(n):
    if not n.count("(") == n.count(")") or "--" in n:
        raise FormatError("Format error")
    
    if not (n[0] == "8" or n[0:2] == "+7"):
        raise CountryCodeError("Country code error")
    
    s = ['-', '+', '(', ')', ' ']
    for _ in s:
        n = n.replace(_, '')
    
    if len(n) != 11:
        raise AmountError("Amount error")

    n = '7' + n[1:]

    providers = ['910', '911', '912', '913', '914', '915', '916', '917', '918', '919']
    for prov in providers:
        if n[1:4] not in providers:
            raise ProviderError('Provider error')
    return f'+{n}'
    
    


if __name__ == "__main__":
    while True:
        n = input('pn: ')
        try:
            print(check_number(n))
        except PhoneException as e:
            print(e)