from itertools import permutations, combinations, combinations_with_replacement
n=int(input())
k=[]
for i in range(0,n):
    word=input()
    perms = [''.join(p) for p in permutations(word)]
    l=list(set(perms))
    l.sort()
    if(word in l):
        m=l.index(word)
        if m==(len(l)-1):
           k.append("no answer")
        else:
            k.append(l[m+1])
    else:
        k.append("no answer")
print('\n'.join(k))