import random 
print('--------------------------------------------------------------------------------------')
#1

movy = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']
print (movy)
movy.sort()
print(movy)
sorted_movy = sorted(movy)
print (sorted_movy)
movy.reverse()
print(movy)

print('---------------------------------------------------------------------------------------')
#2

numbers = list(random.sample(range(0, 1000), random.randint(2, 100)))
print(numbers)
print (sum(numbers))

print('---------------------------------------------------------------------------------------')
#3

cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
print(cities[0], cities[1], cities[2], cities[3], cities[4], sep = ", ", end = " and ")
print(cities[5])

print('---------------------------------------------------------------------------------------')
#4

str = input('String of charachters')
arr1 = str.split()
copy = arr1.copy()
arr2 = (copy[::-1])
con = arr1 + arr2
print("Concatenated arrays:", con)

suma = 0
for i in range(0, len(con)):
  con[i] = int(con[i])
  suma += con[i]
print("\nThe sum of modified array:", suma)

#5

oceans  = ['Atlantic', 'Pacific', 'Indian', 'Arctic']
print (oceans.copy())
print (list(oceans))
print (len(oceans))
print (', '.join(oceans))
print (oceans.index(random.choice(oceans)))
oceans.append('Append')
print(oceans)
oceans.insert(0,'Insert')
print(oceans)
oceans.extend(movy)
print(oceans)
del oceans[-1]
print(oceans)
oceans.remove('Insert')
print(oceans)
print (oceans.pop())
print(oceans.count('Pacific'))
oceans.sort()
print(oceans)
sorted_oceans = sorted(oceans)
print(sorted_oceans)
oceans.reverse()
print(oceans)

print('---------------------------------------------------------------------------------------')

numbers = list(range(1,9))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print('---------------------------------------------------------------------------------------')

#6   
  
keywords = ('for', 'if', 'else', 'in', ':')
for item in keywords:
   print(" " * 4 + item)
