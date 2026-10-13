N = int(input())
S = input()

count = 0
longest = 0

for i in S:
    if i == 'R':
        count += 1
    else:
        if longest < count:
            longest = count
        count = 0
if longest < count:
            longest = count

print(longest)
