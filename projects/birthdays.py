birthdays = {'samko': 'apr 3', 'petko': 'jul 28'}

while True:
    print('enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('i do now have birthday information for ' + name)
        print('what is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('birthday database updated.')
