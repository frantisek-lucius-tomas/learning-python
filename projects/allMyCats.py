catNames = []

while True: 
    print('set name for your cat number ' + str(len(catNames)) + ' for the program to stop enter nothing')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]

print('your cats names are')

for name in catNames:
    print('  ' + name)
