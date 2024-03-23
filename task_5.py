import ru_local as ru

beginning, end = input().split('-')
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
beginning_list = list(beginning)
end_list = list(end)
beginning_letter = beginning_list[0]
beginning_number = int(beginning_list[1])
end_letter = end_list[0]
end_number = int(end_list[1])
beginning_letter_int = dictionary.get(beginning_letter)
end_letter_int = dictionary.get(end_letter)
if abs(end_letter_int - beginning_letter_int) == 1 and abs(end_number - beginning_number) == 2 \
        or abs(end_letter_int - beginning_letter_int) == 2 and abs(end_number - beginning_number) == 1:
    print(ru.CORRECT)
else:
    print(ru.MISTAKE)
