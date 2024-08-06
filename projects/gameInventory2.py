inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(x, addedItems):
    for i in addedItems:
        if i in x:
            x[i] += 1
        
        x.setdefault(i, 1)

addToInventory(inventory, dragonLoot)

def displayInventory(w):
    suM = 0
    print('inventory :')
    for x, y in w.items():
        print('' + str(y) + ' ' + str(x))
        suM += y

    print('total number of items: ' + str(suM))

displayInventory(inventory)
