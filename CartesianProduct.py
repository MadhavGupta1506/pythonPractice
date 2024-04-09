a=list(map(int,input().split()))
b=list(map(int,input().split()))
cartesian=[]
for i in range(len(a)):
    for j in range(len(b)):
        cartesian.append((a[i],b[j]))
for i in cartesian:
    print(i,end=" ")