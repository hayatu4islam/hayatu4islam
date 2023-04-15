# Create generator function
def Items():
    print("First item!")
    yield 15

    print("Second item!")
    yield 25

    print("Third item!")
    yield 40

newGenerator = Items()
print(next(newGenerator))
print(next(newGenerator))

print(next(newGenerator))
print(next(newGenerator))
