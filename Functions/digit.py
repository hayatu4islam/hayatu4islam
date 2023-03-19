def digitNum(num):
    ans = 0
    while num != 0:
        num //= 10
        ans += 1
    return ans
print(digitNum(0))