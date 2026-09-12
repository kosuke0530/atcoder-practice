n = input()
l = [int(x) for x in input().split()]

n100 = 0
n10 = 0
n1 = 0
#lc = 1

for i in l:
    #print(f'{lc}回目のループ')
    #lc += 1
    if i % 1000 == 0:
        continue
    else:
        cost = (i // 1000) + 1
        chan = (cost * 1000) - i
    
    n100 += chan // 100
    chan %= 100
    #print('n100', n100)
    
    n10 += chan // 10
    chan %= 10
    #print('n10', n10)
    
    n1 += chan
    #print('n1', n1)
        
print(n1, n10, n100)