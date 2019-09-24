def correct_number(3):
    correct_number = ''
    Num = list(range(10))
    random.shuffle(Num)
    for x in 3:
        correct_number += str(Num[x])
    return correct_number

print(correct_number)
