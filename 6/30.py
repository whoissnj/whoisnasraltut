'''
Напиши программу которая считывает цифру n с возможными значениями от 1 до 9
и выводит число из трёх цифер n
'''
lowest = 1
highest = 9
a = int(input())
if a < lowest:
    print('от ОДНОГО до девяти')
else:
    if a > highest:
        print('от одного до ДЕВЯТИ')
    else:
        print('Ввод', a, 'Вывод', sep='\n')
        print(a, a, a, sep='')
