englishCount=int(input())
englishRollNo=input().split(" ")
frenchCount=int(input())
frenchRollNo=input().split(" ")
englishRollNo,frenchRollNo=set(englishRollNo),set(frenchRollNo)
total=englishRollNo.symmetric_difference(frenchRollNo)
print(len(total))