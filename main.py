import matplotlib.pyplot as plt
import math
d = int(input())
chislitel1 = d*d - 2000 #раскрытие модуля числителя положительно
chislitel2 = (d*d - 2000) * (-1) #раскрытие модуля числителя отрицательно
x1 = d #раскрытие модуля переменной в знаменателе  положительно
x2 = d * (-1) #раскрытие модуля переменной в знаменателе  отрицательно
znamenatel1 = x1 - 2000
znamenatel2 = x2 - 2000
print("Первое значение:", chislitel1/znamenatel1)
print("Второе значение:", chislitel1/znamenatel2)
print("Третье значение:", chislitel2/znamenatel1)
print("Четвёртое значение:", chislitel2/znamenatel2)