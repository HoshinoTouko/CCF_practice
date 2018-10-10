def _input():
    return list(map(int, input().split()))

n, m = _input()

patterns = []


digits = '0123456789'
letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-_.'

def is_digits(text):
    if len(text) == 0:
        return False
    for i in text:
        if i not in digits:
            return False
    return True


def is_letters(text):
    if len(text) == 0:
        return False
    for i in text:
        if i not in digits and i not in letters:
            return False
    return True


def is_legal(text):
    for i in text:
        if i not in digits and i not in letters and i != '/':
            return False
    return True


def parse(url):
    if not is_legal(url):
        print(404)
        return

    splited_url = url[1:].split('/')

    res = ''
    for pat, name in patterns:
        if '<path>' not in pat and len(pat) != len(splited_url):
            continue
        if len(pat) > len(splited_url):
            continue
        
        res = name
        for pointer in range(len(pat)):
            if pat[pointer] == '<path>':
                res += ' %s' % '/'.join(splited_url[pointer:])
                continue
            if pat[pointer] == '<int>':
                if is_digits(splited_url[pointer]):
                    res += ' %s' % int(splited_url[pointer])
                    continue
                break
            elif pat[pointer] == '<str>':
                if is_letters(splited_url[pointer]):
                    res += ' %s' % splited_url[pointer]
                    continue
                break
            else:
                if pat[pointer] == splited_url[pointer]:
                    continue
                break
        else:
            break
    else:
        res = 404
    
    print(res)


def read_pattern():
    data, name = input().split()

    return (data[1:].split('/'), name)


for _ in range(n):
    patterns.append(read_pattern())

to_parse = []
for _ in range(m):
    to_parse.append(input())

for _parse in to_parse:
    parse(_parse)
