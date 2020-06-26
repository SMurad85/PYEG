
'''Задание 4.1
Обработать строку nat таким образом, чтобы в имени интерфейса 
вместо FastEthernet было GigabitEthernet.
Ограничение: Все задания надо выполнять используя только пройденные темы.'''

# NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
# NAT = NAT.replace('Fast', 'Gigabit')
# print(NAT)


'''Задание 4.2
Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX XXXX.XXXX.XXXX
Ограничение: Все задания надо выполнять используя только пройденные темы.'''

# mac = 'AAAA:BBBB:CCCC'
# mac = mac.replace(':', '.')
# print(mac)



'''Задание 4.3
Получить из строки config список VLANов вида: ['1', '3', '10', '20', '30', '100']
Ограничение: Все задания надо выполнять используя только пройденные темы.'''

# config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
# config = config.split()
# config = config[-1].split(',')
# print(config)



'''Задание 4.4
Список vlans это список VLANов, собранных со всех устройств сети, поэтому 
в списке есть повторяющиеся номера VLAN.
Из списка нужно получить уникальный список VLANов, отсортированный по возрастанию номеров.
Ограничение: Все задания надо выполнять используя только пройденные темы'''

# vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
# vlan = set(vlans)
# print(vlan)




'''Задание 4.5
Из строк command1 и command2 получить список VLANов, которые есть и в команде 
command1 и в команде command2.
Результатом должен быть спи'сок: ['1', '3', '8']
Ограничение: Все задания надо выполнять используя только пройденные темы.'''

# command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
# command2 = 'switchport trunk allowed vlan 1,3,8,9'
# com1 = command1.split()
# com2 = command2.split()
# com11 = com1[-1].split(',')
# com22 = com2[-1].split(',')
# com1122 = list(set(com11) & set(com22))
# print(com1122)





'''Задание 4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Ограничение: Все задания надо выполнять используя только пройденные темы.
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'''

ospf = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf = ospf.split()
ospf = dict.fromkeys(ospf, 0)
print(ospf)

# ospf = ['ip'] = '10.1.1.1'
# print(keys)

# router_mobels = ['ISR2811', 'ISR2911', 'ISR2921', 'ASR9002']
# mobels_count= dict.fromkeys(router_mobels, 0)
# print(mobels_count)

osp = '''
Protocol:               OSPF
Prefix:                 10.0.24.0/24
AD/Metric:              110/41
Next-Hop:               10.0.13.3
Last update:            3d18h
Outbound Interface:     FastEthernet0/0'''
# osp1 = osp.split()
# # osp1 = osp1[:]













'''Задание 4.7
Преобразовать MAC-адрес mac в двоичную строку такого вида: 
101010101010101010111011101110111100110011001100
Ограничение: Все задания надо выполнять используя только пройденные темы'''

# mac = 'AAAA:BBBB:CCCC'
# mac = bin(10)
# mac = int(10)
# print(mac)

# a = '{:08b} {:08b} {:08b} {:08b}'.format(192,168,100,1)
# print(a)
