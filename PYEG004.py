
#Примеры списков 
# list1 = [10,20,30,77]
# list2 = ['one', 'dog', 'seven']
# list3 = [1, 20, 4.0, 'word']


#Создание списка с помощью литерала: Литерал - это выражение, которое создает объект.
# Vlan = [10, 20, 30, 50]

#Создание списка с помощью функции list():
# List1 = list('router')
# print(List1)

# list2 = [1, 20, 4.0, 'word']
# print(list2[1])
# print(list2[1::])
# print(list2[-1])
# print(list2[::-1])


# Перевернуть список наоборот можно и с помощью метода reverse():
# vlans = ['10', '15', '20', '30', '100-200']
# vlans.reverse()
# print(vlans)

# так как списки изменяемые, элементы списка можно менять:
# list4 = [1, 20, 4.0, 'word']
# print(list4)
# list4[0] = 'test'
# print(list4)

# interfaces = [['FastEhernet0/0', '10.0.15.1', 'YES', 'manual', 'up', 'up'],
# ['FastEhernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'],
# ['FastEhernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down']]
# print(interfaces[0][0])
# print(interfaces[2][0])
# print(interfaces[2][1])

# Функция len возвращает количество элементов в списке:
# items = [1, 2, 3]
# print(len(items))

'''А функция sorted сортирует элементы списка по возрастанию и возвращает 
новый список с отсортированными элементами:'''
# names = ['John', 'Michael', 'Antony']
# print(sorted(names))


#Полезные методы для работы со списками
#Метод join() собирает список строк в одну строку с разделителем, который указан перед join:
# vlan = ['10', '20', '30']
# vlan = ','.join(vlan)
# print(vlan)

#Метод append() добавляет в конец списка указанный элемент:
# vlan = ['10', '20', '30', '100-200']
# vlans = vlan.append('300')
# print(vlan)

'''Если нужно объединить два списка, то можно использовать два способа: 
метод extend() и операцию сложения.'''
# vlan = ['10', '20', '30', '100-200']
# vlan2 = ['300', '400', '500']
# vlan3 = vlan.extend(vlan2)
# print(vlan)


'''Метод pop() удаляет элемент, который соответствует указанному номеру. 
Но, что важно, при этом метод возвращает этот элемент:'''
# vlan = ['10', '20', '30', '100-200']
# vlan2 = vlan.pop(-1)
# print(vlan)


'''Метод remove() удаляет указанный элемент.
remove() не возвращает удаленный элемент:'''
# vlan = ['10', '20', '30', '100-200']
# vlan2 = vlan.remove('20')
# print(vlan)


'''Метод index() используется для того, чтобы проверить, 
под каким номером в списке хранится элемент:'''
# vlan = ['10', '20', '30', '100-200']
# vlan2 = vlan.index('30')
# print(vlan)
# print(vlan2)


'''Метод insert() позволяет вставить элемент на определенное место в списке:'''
# vlan = ['10', '20', '30', '100-200']
# vlan2 = vlan.insert(1, '15')
# print(vlan)


'''Метод sort сортирует список на месте:'''
vlan = [1, 50, 10, 15]
vlan2 = vlan.sort()
print(vlan)









