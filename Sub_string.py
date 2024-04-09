def count_substring(string, substring):
    count=0
    for i in range(len(string)):
        if(string[i:len(substring)+i]==substring):
            count+=1
        print(string[i:len(substring)+i])
    return count
string="ABCDCDC"
substring="CDC"
print(count_substring(string,substring))