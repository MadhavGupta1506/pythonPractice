l=input().split()
n=int(l[0])
happiness=0
m=int(l[1])
array=input().split()
A=input().split()
B=input().split()
for i in range(n):
    if(array[i] in A):
        happiness+=1
    elif(array[i] in B):
        happiness-=1
print(happiness)