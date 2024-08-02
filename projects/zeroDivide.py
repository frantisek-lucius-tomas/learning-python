def spam(divideBy):
    try: 
        return 42 / divideBy
    except ZeroDivisionError:
        print('error: Invalid argumen.')

print(spam(2))
print(spam(0))
