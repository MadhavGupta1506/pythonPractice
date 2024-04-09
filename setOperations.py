nSet=int(input())
elementSet=set(map(int,input().split(" ")))
numberOfSet=int(input())
for i in range(numberOfSet):

    operation=list(input().split(" "))
    elementsOtherSet=set(map(int,input().split(" ")))
    if(operation[0]=="intersection_update"):
        elementSet.intersection_update(elementsOtherSet)
    elif(operation[0]=="update"):
        elementSet.update(elementsOtherSet)
    elif(operation[0]=="symmetric_difference_update"):
        elementSet.symmetric_difference_update(elementsOtherSet)        
    elif(operation[0]=="difference_update"):
        elementSet.difference_update(elementsOtherSet)
print(sum(elementSet))        