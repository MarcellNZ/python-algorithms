

test = [1, 2, 3, 4, 5, 6, 7, 8]
n = 5

def chunkingRecursion(array, n):
    if len(array) <= n:
        return [array]
    else:
        return [array[:n]] + chunkingRecursion(array[n:], n)

result = chunkingRecursion(test, n)

print(result)
    

    
    



     
    