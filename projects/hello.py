# this program says hellp and asks for my name.

print('hello, world')
print('what is your name?') # ask for their name

myName = input()

print('it is good to meet you, ' + myName)
print('the lenght of your name is: ' + str(len(myName)))

print('what is your age?') # ask for their age

myAge = input()

print('you will be ' + str(int(myAge) + 1) + ' in a year')
