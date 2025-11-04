# https://codeforces.com/problemset/problem/228/A
# Sets store unique value

colors = list(input().split())
colors = set(colors)

print(4-len(colors))
