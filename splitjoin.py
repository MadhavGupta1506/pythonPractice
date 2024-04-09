l="This is a line"
def split_and_join(line):
    l1=line.split()
    l1="-".join(l1)
    return l1
print(split_and_join(l))