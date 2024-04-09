len_A=(input())
A=set(input().split(" "))
len_B=(input())
B=set(input().split(" "))
temp1=A
temp2=B
A_B=list(map(int,temp1.difference(B)))
B_A=list(map(int,temp2.difference(A)))
symmetricDifference=A_B+B_A
print(symmetricDifference)
for i in range(len(symmetricDifference)):
    for j in range(i+1):
        if(symmetricDifference[i]<symmetricDifference[j]):
            temp=symmetricDifference[i]
            symmetricDifference[i]=symmetricDifference[j]
            symmetricDifference[j]=temp
for i in symmetricDifference:
    print(i)
