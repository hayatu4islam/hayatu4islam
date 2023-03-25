def is_nested(array):
    if len(array) == 0:
        return False
    return all(isinstance(row, list) for row in array)
print(is_nested([[1, 2], [3, 4]]))
print(is_nested([1, [2, 3]]))