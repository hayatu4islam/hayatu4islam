def positiveSum(arr):
    sum = 0
    for x in arr:
        if x > 0:
            sum += x
    return sum
print(positiveSum([1,2,3,4,5]))
print(positiveSum([1,-2,3,4,5]))
print(positiveSum([-1,2,3,4,-5]))