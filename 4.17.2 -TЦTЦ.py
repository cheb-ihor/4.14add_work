#1
names = ['Игорь','Маша','Антон']
names[0]
names[1]
names[2]
#2
transport = ['велосипед','машина','літак', 'вертоліт']
transport_variant = (int (input (" номер, що належить списку transport ")))
"Я хотів би купити " + (transport[transport_variant]) + "."
#3
years_list = [2003,2004,2005,2006,2007,2008]
(years_list[3])
years_list.append(2010)
years_list
max_year = max(years_list)
max_index = years_list.index(max_year)
max_index
years_list[max_index],"рік, це рік в якому мені було найбільше років"
#4
things = ['wallet', 'mirror', 'umbrella']
things[2] = 'Umbrella'
things
things[2] = 'UMBRELLA'
things
del things[2]
things
#5
languages = ['Georgian', 'Estonian', 'Ukrainian']
languages[2] = 'ukrainian'
languages
languages[::-1] 
languages[0] = 'Ukrainian'
languages
#6
hardware = 'ПК', 'програма', 'програмування', 'ЛКМ'
software = ['ПК', 'програма', 'програмування','ЛКМ']
p, pr, pro, lk = hardware
p
pr
pro
lk
software[0]
software[1]
software[2]
software[3]
p = 'пк'
hardware # кортежі є незмінні
software[0] = 'пк'
software # списки є змінні

