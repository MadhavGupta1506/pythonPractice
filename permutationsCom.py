from itertools import combinations
a=input().split()
sort=sorted(list(a[0]))
perlist=[]
for i in range(1,int(a[1])+1):
    perlist+=list(combinations(sort,i))
for i in perlist:
    print("".join(i)) 