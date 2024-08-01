while True:
    print('who r you?')
    name = input()
    if name != 'joe':
        continue
    print("hello, joe. what is the password? (it's is a fish)")
    password = input()
    if password == 'swordfish':
        break
print('access granted')
