n = int(input())
lst = list(map(int, input().split()))

a = max(lst)
b = sum(lst) - a

print(a + (b/2))