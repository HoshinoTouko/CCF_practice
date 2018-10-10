data = list(map(int, input('').split()))

score = 0
loop = 0

for i in data:
    score += i
    if i == 2:
        score += loop * 2
        loop += 1
    else:
        loop = 0

print(score)
