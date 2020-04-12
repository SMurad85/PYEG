'''
sudo apt install python-pip (Установка pip)
pip  install --upgrade pip (обновить pip)

pip  install tabulate  (Установка tabulate)
pip  install --upgrade tabulate (обновить tabulate) 
(tabulate это модуль, который позволяет красиво
отображать табличные данные)

Переключение интерпретатора Python используемого по умолчанию, с версии 2,7 на 3,6
# python --version
#Python 2.7.17
# whereis python3 
Предположим, что вам требуется Python 3.6. Проверим, что он доступен: если интерпретатор не найден, используем apt для его установки
# sudo apt update && sudo apt install python3
Теперь можно переключить версию интерпретатора, выполнив команду ln.
# sudo ln -sfn /usr/bin/python3.6 /usr/bin/python
# python --version
#Python 3.6..9

Интерпретатор python, ipython
Установка ipython
#sudo pip install ipython
После переходим в ipython
#ipython
In [1]:
'''

#Числа - С числами можно выполнять различные математические операции.
# a = 1 + 2
# b = 1.0 + 2
# c = 10 - 4
# d = 2**3
# print(a, b, c, d)

#Деление int и float:
# a = 10/3
# b = 10/3.0
# print(a)

#С помощью функции round можно округлить числа до нужного количества знаков:
# a = round(10/3.0, 2)
# b = round(10/3.0, 4)
# print(a, b)

#Остаток от деления:
# a = 10 % 3
# print(a)

#Операторы сравнения 
# a = 10 > 3.0
# print(a)
# b = 10 < 3
# print(b)
# c = 10 == 3
# print(c)
# d = 10 == 10
# print(d)
# w = 10 <= 10
# print(w)
# v = 10.0 == 10
# print(v)

"""Функция int() позволяет выполнять конвертация в тип int. Во втором 
аргументе можно указывать систему счисления"""
# a = '11'
# int(a)

# int (a, 2)

"""Функция bin позволяет получить двоичное предстовление числа обратите 
внимание, что результат строка"""

# bin(8)
# nex(10)
# print(bin)

#Для более сложных математических функции в Python усть модуль math:
# import math 
# a= math.sqrt(9)
# print(a)


#СТРОКИ(Strings)
"""Строка в Python это: 
-Последовательность символов, заключенная в кавычки. 
-неизменяемый упорядоченный тип данных"""
# a = 'Hello'
# print(a)

# tunnel = """interface Tunnel0
# ip address 10.10.10.1 255.255.255.0
# ip mtu 1416
# ip ospf hello-interval 5
# tunnel source FastEthernet1/0
# tunnel protection ipsec profile DMVPN
# """
# print(tunnel)

#Строки можно суммировать в одну строку.
# intf = 'interface'
# tun = 'Tunnel0'
# print(intf + tun)
# print(intf +' '+ tun)

#Строки можно умножить на числа.
# a = 'строка' * 5
# print(a)

'''То, что строки являются упорядоченным типом данных, позволяет 
обращаться к символам в строке по номеру, начиная с нуля:'''
# string1 = 'interface FastEthernet'
# print(string1[0])

"""Но, если нужно обратиться к какому-то по счету символу, начиная с конца, то можно 
указывать отрицательные значения (на этот раз с единицы)."""
# print(string1[1])
# print(string1[-1])
# print(string1[0:9])
# print(string1[10:22])
#Так можно получить нечетные числа:
# a = '0123456789'
# print(a[1::2])
# print(a[::2])
# print(a[::-1])

#Функция len позволяет получить количество символов в строке:
line = 'interfaceGi0/1'
print(len(line))






