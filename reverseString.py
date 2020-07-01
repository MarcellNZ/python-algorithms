


def reverseBuiltIn(unreversedArray):
    unreversedArray.reverse()
    return ''.join(unreversedArray)

def reverseLoop(unreversedArray):
    result = ''
    for char in unreversedArray:
        result = char + result
    return result
    
def reverseIndex(unreversedArray):
    return ''.join(unreversedArray[::-1])

def reverseRecursion(unreversedArray):
    arrayLen = len(unreversedArray)

    if arrayLen == 1:
        return unreversedArray[arrayLen-1]
    elif arrayLen == 2:
        return unreversedArray[arrayLen-1] + unreversedArray[0]
    else:
        midpoint = len(unreversedArray)//2
        return reverseRecursion(unreversedArray[midpoint+1:]) + unreversedArray[midpoint] + reverseRecursion(unreversedArray[:midpoint])

    return ''.join(unreversedArray)

for func in [reverseBuiltIn, reverseLoop, reverseIndex, reverseRecursion]:
    unreversedArray = list('reversed')
    print(func(unreversedArray))



