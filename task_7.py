import ru_local as ru

sushi_k = int(input())
way = 0
for x in range(0, 100):
    for y in range(0, 100):
        if sushi_k == 5*x + 7*y:
            way += 1
if way > 0:
    print(ru.YES)
else:
    print(ru.NO)
