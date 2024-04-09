l=[1,2,3,4,6,7,9,10,12,17,20,99]
start=0
end=len(l)-1
def binary(start,end,l,m):
    mid=int((start+end)/2)
    while(start<=end):
        if(l[mid]==m):
            return mid
        elif(l[mid]<m):
            start=mid+1
            return binary(start,end,l,m)
        else:
            end=mid-1
            return binary(start,end,l,m)
print(binary(start,end,l,15))