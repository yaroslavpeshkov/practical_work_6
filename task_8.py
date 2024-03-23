number = int(input())
numbers = [0]
for i in range(0, 201):
    numbers_i = []
    while i > 0:
        i_1 = i % 10
        numbers_i.append(i_1)
        i = i // 10
    numbers_i.reverse()
    numbers = numbers + numbers_i
print(numbers[number - 1])
