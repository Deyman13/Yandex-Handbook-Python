a, b, c, d = map(int, input().split())
l = []
l.append(max(a, c) * (b + d))
l.append(max(a, d) * (b + c))
l.append(max(b, c) * (a + d))
l.append(max(b, d) * (a + c))
if min(l) == l[0]:
    print(max(a, c), b + d)
elif min(l) == l[1]:
    print(max(a, d), b + c)
elif min(l) == l[2]:
    print(max(b, c), a + d)
else:
    print(max(b, d), a + c)

        
    
    






