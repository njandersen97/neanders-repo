def coma():
    if len(spam) > 2:
        for i in range(len(spam) - 2):
            print(spam[i] + ', ', end='')
        print(spam[-2] + ', and ' + spam[-1])
    elif len(spam) == 2:
        print(spam[0] + ' and ' + spam[1], end='')
    else:
        print('Too few items for a list')

print('Please enter your list with only spaces between the values:')
input_spam = input()
spam = input_spam.split()

coma()
