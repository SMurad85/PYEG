'''Словарь (Dictionary)

Словари - это изменяемый упорядоченный тип данных:

    данные в словаре - это пары ключ: значение
    доступ к значениям осуществляется по ключу, а не по номеру, как в списках
    данные в словаре упорядочены по порядку добавления элементов
    так как словари изменяемы, то элементы словаря можно менять, добавлять, удалять
    ключ должен быть объектом неизменяемого типа: число, строка, кортеж
    значение может быть данными любого типа
'''
'''Пример словаря:'''
# london = {'name': 'London1', 'location', 'London Str', 'vendor': 'Cisco'}

'''Можно записывать и так'''
# london = {
#     'id': 1,
#     'name':'London',
#     'it_vlan':320,
#     'user_vlan':1010,
#     'mhgmt_vlan':99,
#     'to_name': None,
#     'to_id': None,
#     'port':'G1/0/11'
# }


'''Для того, чтобы получить значение из словаря, надо обратиться по ключу, таким же 
образом, как это было в списках, только вместо номера будет использоваться ключ:'''

# london = {'name': 'London1', 'location':'London Str'}
# print(london['name'])
# print(london['location'])


'''Аналогичным образом можно добавить новую пару ключ-значение:'''

# london['vendor'] = 'Cisco'
# print(london)

'''В словаре в качестве значения можно использовать словарь:'''

# london_co = {
#     'r1': {
#         'hostname': 'london_r1',
#         'location': '21 New Globe Walk',
#         'vendor': 'Cisco',
#         'model': '4451',
#         'ios': '15.4',
#         'ip': '10.255.0.1'
#     },
#     'r2': {
#         'hostname': 'london_r2',
#         'location': '21 New Globe Walk',
#         'vendor': 'Cisco',
#         'model': '4451',
#         'ios': '15.4',
#         'ip': '10.255.0.1'
#     },
#     'sw1': {
#         'hostname': 'london_sw1',
#         'location': '21 New Globe Walk',
#         'vendor': 'Cisco',
#         'model': '3850',
#         'ios': '3.6.XE',
#         'ip': '10.255.0.101'
    # }
# }
                        #Получить значения из вложенного словаря можно так:
# print(london_co['r1']['ios'])
# print(london_co['r1']['model'])
# print(london_co['sw1']['ip'])


'''Функция sorted сортирует ключи словаря по возрастанию и возвращает 
новый список с отсортированными ключами:'''

# london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
# lonSort = sorted(london)
# print(lonSort)


'''Полезные методы для работы со словарями
clear()'''

# london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
# london = london.clear()
# print(london)


'''copy()
Метод copy() позволяет создать полную копию словаря.
Если указать, что один словарь равен другому:'''

# london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
# london2 = london
# print (id(london))
# print (id(london2))
# london3 = london['vendor'] = 'Juniper'
# print(london2['vendor'])
'''В этом случае london2 это еще одно имя, которое ссылается на словарь. И при 
изменениях словаря london меняется и словарь london2, так как это ссылки на 
один и тот же объект.
Поэтому, если нужно сделать копию словаря, надо использовать метод copy():'''

# london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
# london2 = london.copy()
# print (id(london))
# print (id(london2))
# london3 = london['vendor'] = 'Juniper'
# print(london2['vendor'])



'''get()
Если при обращении к словарю указывается ключ, которого нет в словаре, возникает ошибка:'''

# london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
# print(london['ios'])

'''Метод get() запрашивает ключ, и если его нет, вместо ошибки возвращает None.'''

# london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
# print(london.get('ios'))  #None
# '''Метод get() позволяет также указывать другое значение вместо None:'''
# print(london.get('ios', 'Ooops')) #Opps



'''Метод setdefault() ищет ключ, и если его нет, вместо ошибки создает 
ключ со значением None.'''

# london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco3580'}
# ios = london.setdefault('ios')
# print(ios) #None
'''Если ключ есть, setdefault возвращает значение, которое ему соответствует:'''
# print(london.setdefault('name')) #London1
'''Второй аргумент позволяет указать, какое значение должно соответствовать ключу:'''
# model = london.setdefault('model', 'Cisco')
# print(model)
# print(london)

'''Метод setdefault заменяет такую конструкцию:
if key in london:
    value = london:[key]
else:
    london[key] = 'somevalue'
    value = london[key]'''



'''keys(), values(), items()
Методы keys(), values(), items():'''
# london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco3580'}
# print(london.keys())   #dict_keys(['name', 'location', 'vendor'])
# print(london.values()) #dict_values(['London1', 'London Str', 'Cisco3580'])
# print(london.items())  #dict_items([('name', 'London1'), ('location', 'London Str'), ('vendor', 'Cisco3580')])
'''Все три метода возвращают специальные объекты view, которые отображают 
ключи, значения и пары ключ-значение словаря соответственно.
Очень важная особенность view заключается в том, что они меняются вместе с 
изменением словаря. И фактически они лишь дают способ посмотреть на 
соответствующие объекты, но не создают их копию.

На примере метода keys():'''
# london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco3580'}
# # keys = london.keys()
# # print(keys)
'''Сейчас переменной keys соответствует view dict_keys, в котором три ключа: 
name, location и vendor.
Но, если мы добавим в словарь еще одну пару ключ-значение, объект 
keys тоже поменяется:'''
# london['ip'] = '10.1.1.1'
# print(keys)
'''Если нужно получить обычный список ключей, который не будет меняться с изменениями 
словаря, достаточно конвертировать view в список:'''
# list_keys = list(london.keys())
# print(list_keys)



'''del
Удалить ключ и значение:'''
# london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco3580'}
# del london['name']
# print(london)



'''update
Метод update позволяет добавлять в словарь содержимое другого словаря:'''
# r1 = {'name': 'London1', 'location': 'London Str'}
# print(r1)
# r1.update({'vendor': 'Cisco3580', 'ios': '15.2'})
# print(r1)
'''Аналогичным образом можно обновить значения:'''
# r1.update({'name': 'London-r1', 'ios': '15.4'})
# print(r1)



'''Варианты создания словаря
Литерал
Словарь можно создать с помощью литерала:'''
# r1 = {'model': '4451', 'ios': '15.4'}
# print(r1)


'''dict
Конструктор dict позволяет создавать словарь несколькими способами.
Если в роли ключей используются строки, можно использовать такой вариант создания словаря:'''
# r1 = dict(model = '4451', ios = '15.4')
# print(r1)


'''Второй вариант создания словаря с помощью dict:'''
# r1 = dict([('model', '4451'), ('ios', '15.4')])
# print(r1)


'''dict.fromkey
В ситуации, когда надо создать словарь с известными ключами, но пока что 
пустыми значениями (или одинаковыми значениями), очень удобен метод fromkeys():'''
# d_keys = ['hostname', 'location', 'vendor', 'ios', 'ip']
# r1 = dict.fromkeys(d_keys)
# print(r1)

'''По умолчанию метод fromkeys подставляет значение None. Но можно 
указывать и свой вариант значения:'''
# router_mobels = ['ISR2811', 'ISR2911', 'ISR2921', 'ASR9002']
# mobels_count= dict.fromkeys(router_mobels, 0)
# print(mobels_count)

'''Этот вариант создания словаря подходит не для всех случаев. Например, при 
использовании изменяемого типа данных в значении, будет создана 
ссылка на один и тот же объект:'''
router_mobels = ['ISR2811', 'ISR2911', 'ISR2921', 'ASR9002']
routers = dict.fromkeys(router_mobels, [])
print(routers)
routers['ASR9002'].append('london_r1')
print(routers)



















