'''
Напиши программу которая считает стоимость трёх пк состоящих из системника, монитора, клавиатуры и мыши
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
comp = a + b + c + d
print('стоимость состовляющих', a, b, c, d, sep='\n')
print('итоговая стоимость сборки', comp, sep='\n')