#https://codeforces.com/problemset/problem/61/A
#using properties of string

num1 = input()
num2 = input()

n = len(num1)
num = [0] * n

for c in range(n):
    if num1[c] == num2[c]:
        num[c] = 0
    else :
        num[c] = 1
print(''.join(str(x) for x in num))

