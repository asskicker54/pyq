import re
import pytest

def fun(s):
    correct_email = r"^[a-zA-Z|\d|_|-]+\@[a-zA-Z|\d]+\.[a-zA-Z]{1,3}$"
    
    if re.search(correct_email, s) == None:
        return False
    return True

def filter_mail(emails):
    return list(sorted(filter(fun, emails)))

def main():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = filter_mail(emails)
    print(filtered_emails)
    
def test():
    for i in range(10):
        with open(f'./email_test/input/input0{i}.txt', 'r') as fi:
            with open(f'./email_test/output/output0{i}.txt', 'r') as fo:
                fi.read(2)
                assert str(filter_mail(fi.read().splitlines())) == fo.read()
    
if __name__ == '__main__':
    test()