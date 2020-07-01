

def multipleOfTwo(num, first, second):
    if (num % first == 0 and num % second == 0):
        print('%s Multiple of both' % (num))
    elif (num % first == 0):
        print('%s Multiple of %s' % (num, first))
    elif (num % second == 0):
        print('%s Multiple of %s' % (num, second))
    else:
        print('none')

for num in range(100):
    multipleOfTwo(num, 3, 5)
