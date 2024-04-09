englishCount=int(input())
englishRollNo=input().split(" ")
frenchCount=int(input())
frenchRollNo=input().split(" ")
englishRollNo,frenchRollNo=set(englishRollNo),set(frenchRollNo)
total=englishRollNo|frenchRollNo
print(len(total))