import re

def strip_punctuation_ru(data):
    if len(data) == 0:
        return data
    else:
        data = ' '.join(data.split())
        res = re.sub(r'\s\W\s|[.,!]', ' ', data)
        return res[:-1] if res[len(res) - 1] == ' ' else res 


def my_test_strip_punctuation_ru():
    test_cases = (
        # simple boundary case
        ('', ''),
        # "subtle" case --word with dash
        ('слов с дефисами видимо-невидимо', 'слов с дефисами видимо-невидимо'),
        # dash needs to be removed
        ('здесь - уже не дефис', 'здесь уже не дефис'),
        # ordinary case
        ('Эта строка не изменится', 'Эта строка не изменится'),
        # no punctuation
        ('здесь нет     пунктуации', 'здесь нет пунктуации'),
        ('много,разной.пунктуации!', 'много разной пунктуации'),
        ('Москва - моя родина', 'Москва моя родина')
    )

    for in_s, correct_out_s in test_cases:
        out_s = strip_punctuation_ru(in_s)
        if out_s != correct_out_s:
            print(out_s, correct_out_s)
            return False
    return True

print("YES") if my_test_strip_punctuation_ru() else print("NO")
