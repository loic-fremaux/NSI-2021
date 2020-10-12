total = 0

for i in range(1000, 10_000):
    nbrAsStr = str(i)
    sum = 0
    for s in nbrAsStr:
        sum += int(s)
    if sum % 10 == 0:
        total += 1
