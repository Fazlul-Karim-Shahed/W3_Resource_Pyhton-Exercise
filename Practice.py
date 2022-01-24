
def sumOfInteger(digit):
    list = []
    sum  = 0
    d = digit
    for i in range(digit):         #123
        r = d % 10
        sum = sum + r
        d = int(d / 10)

        if d == 0:
            break
    return sum

print(sumOfInteger(5))
