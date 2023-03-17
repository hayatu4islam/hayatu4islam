def OddorEven(num):
    sum = 0
    for x in num:
        sum += x
    if sum % 2 == 0:
        return "Even"
    return "Odd"
print(OddorEven([1,2,3,4,5]))