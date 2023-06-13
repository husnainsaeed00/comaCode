spam = ['apples', 'bananas', 'tofu', 'cats']

def comacode(spam):
    for i in range(len(spam)):
        val = str(spam[i])
        for j in val:
            print(j+',', end='')
        print()
comacode(spam)