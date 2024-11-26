immutable_var = ([1,2,3],"привет")
print(immutable_var)
#immutable_var[1]=25
#print(immutable_var)

mutable_list=["сорок_восемь_попугаев", 25, 'нет']
print(mutable_list)
mutable_list[0]="нет никаких попугаев"
print(mutable_list)
mutable_list[2]="двадцать один попугайчик " + (str(43))
print(mutable_list)