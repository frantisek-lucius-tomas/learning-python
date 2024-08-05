myPets = ['beja', 'tobka', 'kika']

print('enter a pet name:')
name = input()

if name not in myPets:
    print('i do not have a pet name ' + name + '.')
else: 
    print(name + ' is my pet.')
