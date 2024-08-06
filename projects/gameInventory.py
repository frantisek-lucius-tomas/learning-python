inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(w):
    suM = 0
    print('inventory :')
    for x, y in w.items():
        print('' + str(y) + ' ' + str(x))
        suM += y

    print('total number of items: ' + str(suM))


displayInventory(inventory)
