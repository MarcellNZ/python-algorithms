n = 3

for x in range(n):
    temp = x + 1
    result = ''
    for _ in range(n):
        if temp > 0:
            result += '#'
            temp -= 1
    print(result)