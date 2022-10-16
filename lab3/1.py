def len_check(p):
    return len(p) > 8

def lowercase_check(p):
    return any(s.lower() for s in p)

def uppercase_check(p):
    return any(s.isupper() for s in p)

def digits_check(p):
    return any(s.isdigit() for s in p)

def dif_check(p):
    bad_passwords = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
    for bp in bad_passwords:
        for i in range(len(bp) - 2):
            if bp[i:i+3] in p:
                return False

    return True

while True:
    p = input('password: ')
    if len_check(p) and lowercase_check(p) and uppercase_check(p) and digits_check(p) and dif_check(p):
        print('ok')
    else:
        print('error')