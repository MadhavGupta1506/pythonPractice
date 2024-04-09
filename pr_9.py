l=[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l2=[]
f=0
count=0
for i in l:
    if(i not in l2):
        l2.append(i)
        count=count+1
for j in range(len(l)):
    if(l[i]==l[i+1]):
        f=1
        break;
if(f==0) and(count==4):
    print(True)    
else:
    print(False)
