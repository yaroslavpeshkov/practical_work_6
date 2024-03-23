import ru_local as ru

square = list(input())
letter = square[0]
number = int(square[1])
if letter == 'a' or letter == 'c' or letter == 'e' or letter == 'g':
    letter = 0
else:
    letter = 1
if (-1)**(letter + number) < 0:
    print(ru.BLACK)
else:
    print(ru.WHITE)
