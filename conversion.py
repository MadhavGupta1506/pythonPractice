n=int(input())
width = len(bin(n)[2:])
def binary(n):
    l=[]    
    while(n>0):
        l.append(str(n%2))        
        n=int(n/2)
    l.reverse()
    return "".join(l)
def octal(n):
    l=[]
    if(n<8):
        return n
    while(n>0):
            l.append(str(n%8))
            n=int(n/8)
    l.reverse()
    return "".join(l)
def Hexa(n):
    l=[]
    dic={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    if(n<16):
        return n
    while(n>0):
        if(n<16 and n>9):
            l.append(dic[n])
            break    
        l.append(str(n%16))
        n=int(n/16)
    l.reverse()
    return "".join(l)
for i in range(1,n+1):
    print(f"{str(i).rjust(width)}  {str(octal(i)).rjust(width)}  {str(Hexa(i)).rjust(width)}  {str(binary(i)).rjust(width)}")
# print(binary(n),octal(10),Hexa(17))