#List Methods .append() , .pop(), .clear(), .copy() , change item, len(), extend(), insert(), .count()
my_list = ['terraform','aws','linux','devops', 2, 5.6, True, 2, 1 , 1]
print(len(my_list))

my_list.append("houston")
my_list.pop()
print(my_list)
my_list[0]='Terraform'
print(my_list[2].upper())

my_list.extend([10,58,78])


my_list.insert(1, 'serge')
print(my_list)