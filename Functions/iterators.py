# fruitstuple = ("banana", "apple", "orange", "pear", "grape")
# newit = iter(fruitstuple)
# for i in newit:
#     print(next(newit))


# Iterator from sequence of characters
# fruitstr ="lemon"
# newit = iter(fruitstr)

# print(next(newit))
# print(next(newit))
# print(next(newit))
# print(next(newit))
# print(next(newit))

# for loop to iterate through a tuple
# fruitstuple = ("banana", "apple", "orange", "pear", "grape")
# for i in fruitstuple:
#     print(i)

# for loop to iterate through a string
# fruitstr ="lemon"
# for i in fruitstr:
#     print(i)

# Build an iterator that returns number
class Counting:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 19:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
newObj = Counting()
newIter = iter(newObj)

print(next(newIter))
print(next(newIter))
print(next(newIter))
print(next(newIter))
print(next(newIter))
print(next(newIter))