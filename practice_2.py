n=int(input("Enter the length of list:"))
l=[]
for i in range(n):
    ele=int(input("Enter element in list:"))
    l.append(ele)
count=0
for i in l:
    if(i==l[4]):
        count+=1
if(count>=3 and n==8):
    print(True)
else:
    print(False)