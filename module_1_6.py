#phone_book={'Rustam':89186503347, "Lola":88005553535} #менять ключ нельзя на другой тип данных
#phone_book['Rustam']=562 #можем менять значение ключа
#phone_book['Dima']=55535658
#del phone_book['Dima'] можно удалять данные из словаря
#phone_book.update({'Sasha':8918652335, 'Alex': 8895124}) # можно добавлять элементы по несколько штук
#print(phone_book.get('Michel', 'Такого ключа нет'))
#a=phone_book.pop('Lola')
#print(a)
#print(phone_book.keys()) достает ключи
#print(phone_book.items())
#set_={1, 2, 3, 4, 6, 6, 4, 2, 'privet', True, (1, 3, 4)}
#list= [1, 2, 1, 2, 3, 3, 4, 2]
#list=set(list)
#(list)
#print(list.add(5))
#print(list)


my_dict={'Рустам': 2002, 'Lola': 2002, 'Denis': 2001}
print(my_dict['Рустам'])
print(my_dict.get('Peter', 'Такого ключа нет'))
my_dict.update({'Peter': 1995, 'Sonya': 2003})
a = my_dict.pop('Peter')
print(a)
print(my_dict)

my_set={1,2,1,2,1,2,3,3,4,4,5,5,5}
print(my_set.add(6))
print(my_set.add(7))
print(my_set)
print(my_set.remove(6))
print(my_set)

