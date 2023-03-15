def multiplyAll(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
print(multiplyAll((8,2,3,-1,7)))