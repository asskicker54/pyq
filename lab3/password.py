class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

class SequenceError(PasswordError):
    pass

def check_password(p):
    if not len(p) > 8:
        raise LengthError("Length error")
    
    if not any(s.islower() for s in p):
        raise LetterError("Lowercase error")

    if not any(s.isupper() for s in p):
        raise LetterError("Uppercase error")


    if not any(s.isdigit() for s in p):
        raise DigitError("Digit error")

    bad  = True
    bad_passwords = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
    for bp in bad_passwords:
        for i in range(len(bp) - 2):
            if bp[i:i+3] in p:
                bad =  False
    
    if not bad:
        raise SequenceError("Bad password")
   
    return "OK"

if __name__ == '__main__':
    while True:
        p = input('password: ')
        try:
            print(check_password(p))
        except PasswordError as err:
            print(err)