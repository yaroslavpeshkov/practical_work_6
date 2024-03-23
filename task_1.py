import ru_local as ru

length, width = map(float, input().split('x'))
if 6.5 >= ((length**2 + width**2)**0.5 / 2):
    print(ru.YES)
else:
    print(ru.NO)
