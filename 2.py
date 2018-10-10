def _input():
    return list(map(int, input().split()))

n, l, t = _input()
data = _input()

direction = [
    1
    for _ in range(n)
]

for _ in range(t):
    for i in range(n):
        data[i] += direction[i]
    for i in range(n):
        if data[i] == 0 or data[i] == l:
            direction[i] *= -1
        for j in range(i, n):
            if data[i] == data[j]:
                direction[i] *= -1
                direction[j] *= -1

data_str = list(map(str, data))
print(' '.join(data_str))
