n = int(input())
data = list(map(int, input().split()))

data = sorted(data)
MIN = data[1] - data[0]

for i in range(len(data) - 1):
    _t = data[i+1] - data[i]
    if _t < MIN:
        MIN = _t

print(MIN)
