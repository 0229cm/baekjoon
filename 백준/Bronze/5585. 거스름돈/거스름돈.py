n = int(input())
n = 1000-n
ans = 0
for i in [500, 100, 50, 10, 5, 1]:
    ans += n//i
    n %= i
print(ans)