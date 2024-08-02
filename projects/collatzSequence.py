# practice projects

def collatz(number):
    global userNumber
    if number % 2 == 0:
        number = number // 2
        userNumber = number
        print(number)
    else:
        number = 3 * number + 1
        userNumber = number
        print(number)
    
print('type your number')
userNumber = int(input())

while userNumber != 1:
    collatz(userNumber)
