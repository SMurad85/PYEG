"""Полезные методы для работы со строками

Строки неизменяемый тип данных, поэтому все методы, которые преобразуют строку 
возвращают новую строку, а исходная строка остается неизменной.
Методы upper, lower, swapcase, capitalize

Методы upper(), lower(), swapcase(), capitalize() выполняют преобразование 
регистра строки:

-upper верхний
-lower ниже
-swapcase
-capitalize капитализировать
"""

# string1 = 'FastEthernet'
# print(string1.upper())
# print(string1.lower())
# print(string1.swapcase())
# print(string1.capitalize())

# string2 = 'Fastethernet'
# string2 = string2.upper()
# print(string2)

"""Метод count
Метод count() используется для подсчета того, сколько 
раз символ или подстрока встречаются в строке:
"""
# string3 = 'Hello, hello, hello, hello'
# string3 = string3.count('hello')
# string3 = string3.count('ello')
# string3 = string3.count('l')
# print(string3)

"""Метод find
Методу find() можно передать подстроку или символ, и он покажет, на 
какой позиции находится первый символ подстроки (для первого совпадения):
Если совпадение не найдено, метод find возвращает -1.
"""
# string4 = 'interface FastEhernet0/1'
# string4 = string4.find('Fast')
# print(string4)

"""Методы startswith, endswith
Проверка на то, начинается или заканчивается ли строка на определенные 
символы (методы startswith(), endswith()):
"""
# string5 = 'FastEthernet0/1'
# string5 = string5.startswith('Fast')
# string5 = string5.startswith('fast')
# string5 = string5.endswith('0/1')
# string5 = string5.endswith('0/2')
# print(string5)

"""Метод replace
Замена последовательности символов в строке на другую 
последовательность (метод replace()):"""
# string6 = 'FastEthernet0/1'
# string6 = string6.replace('Fast', 'Gigabit')
# print(string6)

"""Метод strip
Часто при обработке файла файл открывается построчно. Но в конце 
каждой строки, как правило, есть какие-то спецсимволы (а могут быть и в 
начале). Например, перевод строки.
Для того, чтобы избавиться от них, очень удобно использовать метод strip():
Метод strip() убирает спецсимволы и в начале, и в конце строки. 

Если необходимо убрать символы только слева или только справа, 
можно использовать, соответственно, методы lstrip() и rstrip().
"""
# string7 = '\n\tinterface FastEthernet1\n'
# string7 = string7.strip()
# print(string7)

# string7 = '[110/1045'
# string7 = string7.strip('[]')
# print(string7)

"""Метод Split
Метод split() разбивает строку на части, используя как разделитель 
какой-то символ (или символы) и возвращает список строк:
"""
# string8 = 'switchport trunk allowed vlan 10,20,30,100-200'
# commands = string8.split()
# print(commands)

# vlans = commands[-1].split(',')
# print(vlans)

# string9 = 'switchport trunk allowed vlan 10,20,30,100-200'
# string9 = string9.split()
# print(string9)

# sh_ip_int_e_s = 'switchport trunk allowed vlan 10,20,30,100-200'
# sh_ip_int_e_s.split()
# print(sh_ip_int_e_s)

sh_ip_int_e_s = (' ')
sh_ip_int_e_s.split()
print(sh_ip_int_e_s)










