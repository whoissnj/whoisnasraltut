'''
Напиши программу которая будет высчитывать объем куба и площадь его полной поверхности
по введённому значению длинны ребра
'''
r1 = int(input())
sqr = r1 ** 2 * 6
vol = r1 ** 3
print('Площадь поверхности куба равна', sqr)
print('Объём куба равен', vol)