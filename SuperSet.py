A=list(set(map(int,input().split())))
numberOfTestCase=int(input())
f=True
for i in range(numberOfTestCase):
    B=list(set(map(int,input().split())))
    for i in B:
        if(B not in A)or(len(B)==A):
            f=False
print(f)