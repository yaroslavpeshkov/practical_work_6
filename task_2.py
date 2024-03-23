import ru_local as ru

size_a, size_b = map(float, input().split('x'))
size_c, size_d, size_e = map(float, input().split('x'))
if ((min(size_a, size_b) >= min(size_c, size_d) and max(size_a, size_b) >= max(size_c, size_d)) or
        (min(size_a, size_b) >= min(size_d, size_e) and max(size_a, size_b) >= max(size_d, size_e)) or
        (min(size_a, size_b) >= min(size_c, size_e) and max(size_a, size_b) >= max(size_c, size_e))):
    print(ru.YES)
else:
    print(ru.NO)
