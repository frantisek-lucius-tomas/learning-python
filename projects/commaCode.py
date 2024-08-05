spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(theList):
    theLastItem = theList[-1]
    print(', '.join(theList[:-1]) + ', and ' + theLastItem)

commaCode(spam)
