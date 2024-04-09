def wrap(string, max_width):
    string=list(string)
    count_col=0
    l1=[]
    while(count_col!=len(string)):
        if(count_col% (max_width)!=0 or count_col==0):
            l1.append(string[count_col])
        else:
            l1.append("\n"+string[count_col])
        count_col+=1
    return "".join(l1)
string="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
print(wrap(string,4))