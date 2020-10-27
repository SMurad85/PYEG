# Kontrol hoda programma -06 lekciya

#Раздилить ip на актеты
ip = '10.1.1.1'
# ipp = ip.split('.')
# print (ipp)
print (ip.split('.'))

#Удалить ковычки
octets = ip.split('.')
print (octets)

octets[0] = int(octets[0])
octets[1] = int(octets[1])
octets[2] = int(octets[2])
octets[3] = int(octets[3])
print (octets)

# Объединть актеты
octets[0] = bin(octets[0])[2:]
print (octets)
#-------------------------------

a = 5 
if a == 5:
    print('a ravno 5')

if a == 5:
    print('#'*40)
    print('a ravno 5')
#-------------------------------

if a == 5:
    print('#'*40)
    print('a ravno 5')
else:
    print('a ne ravno 5')
#-------------------------------

if a == 100:
    print('#'*40)
    print('a ravno 5')
elif a == 0:
    print('a ravno o')
elif a == 1:
    print('a ravno 1')
    pass
else:
    print('a ne ravno 5')
#-------------------------------

# d = {5: 'a ravno 5', 0: 'a ravno 0', 1: 'a ravno 1'}
# user_input = input(input('Vvedite chislo: '))
# print(d.get(user_input, 'b ne ravno 0, 1, 5,'))
# ne srabotal (31:45)
#-------------------------------

item = 10
items = [1 ,2, 10, 100]
print(item in items)
    # item (10) есть в этом списке items(1 ,2, 10, 100)
    # Усли есть True то Если нет то False

print (10 in {1,2,3,4})

print (10 in (1,2,3,4))

b = {1: 100, 2: 200, 3:300}
print (100 in b)
print (100 in b.keys())
print (1 in b.keys())
print (1 in b)
#35:07






















