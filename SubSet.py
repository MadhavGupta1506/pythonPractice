numberOfTestCase=int(input())
for i in range(numberOfTestCase):
    numberA=int(input())
    A=list(set(map(int,input().split())))
    numberB=int(input())
    B=list(set(map(int,input().split())))
    for i in A:
        if(i not in B):
            print(False)
        else:
            print(True)
    