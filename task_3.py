import ru_local as ru

quarter_n, quarter_m = map(int, input().split('x'))
quarter_k = int(input())
ways_1 = 0
ways_2 = 0
for i in range(1, quarter_n):
    quarters_1 = i*quarter_m
    if quarters_1 == quarter_k:
        ways_1 += 1
for i in range(1, quarter_m):
    quarters_2 = i*quarter_n
    if quarters_2 == quarter_k:
        ways_2 += 1
if ways_1 + ways_2 == 0:
    print(ru.NOT_FEASIBLE)
else:
    print(ru.SUCCESSFULLY)
