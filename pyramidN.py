n = 3

for x in range(n):
    result = ' '*(n-x-1) + '#'*x + '#' + '#'*x + ' '*(n-x-1)
    print(result)