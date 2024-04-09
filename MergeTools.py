string="AABBAAC"
k=1
l1=[]

if(k==1):
    for i in String:
        print(i)
else:
    for i in range(0,len(String),k):
        l1=list(String[i:k])
        unique=[]
        for i in l1:
            if(i not in unique):
                unique.append(i)
        unique="".join(unique)
        print(unique)
        k=k+k


def merge_the_tools(String, k):
    l1=[]

    if(k==1):
        for i in String:
            print(i)
    else:
        for i in range(0,len(String),k):
            l1=list(String[i:k])
            unique=[]
            for i in l1:
                if(i not in unique):
                    unique.append(i)
            unique="".join(unique)
            print(unique)
            k=k+k
