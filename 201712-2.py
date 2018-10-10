n, k = list(map(int, input().split()))

_k1 = 0 # Mod
_k2 = 0 # Position

def add(_k1, _k2):
    res = False
    _k1 += 1
    _k2 += 1
    if _k1 == k:
        _k1 = 0
        res = True
    if _k2 == k:
        res = True
    elif _k2 == 10:
        _k2 = 0
    return res, _k1, _k2

children = [
    i + 1
    for i in range(n)
]

pointer = 0
while(len(children) > 1):
    res, _k1, _k2 = add(_k1, _k2)
    if res:
        children.pop(pointer)
    else:
        pointer += 1
    
    if pointer >= len(children):
        pointer -= len(children)

print(children[0])
