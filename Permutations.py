from itertools import permutations
a=input().split()
sort=sorted(list(a[0]))
perlist=list(permutations(sort,int(a[1])))
for i in perlist:
    print("".join(i)) 