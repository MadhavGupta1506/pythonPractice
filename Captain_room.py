# number=int(input())
# roomsOfMembers=list(map(int,input().split()))
# distinctRooms=list(set(roomsOfMembers))
# print(distinctRooms)
# finalList=[]
# roomsOfMembers=sorted(roomsOfMembers)
# for i in range(len(distinctRooms)):
#     l1=[]
#     for j in range(len(roomsOfMembers)):
#         if(distinctRooms[i]==roomsOfMembers[j]):
#             l1.append(roomsOfMembers[j])
#     finalList.append(l1)
# for i in range(len(finalList)):
#     if(len(finalList[i])!=number):
#         print(finalList[i][0])

number=int(input())
roomsOfMembers=list(map(int,input().split()))
Unique=set()
Duplicate=set()
for i in roomsOfMembers:
    if(i in Unique):
        Unique.remove(i)
        Duplicate.add(i)
    else:
        Unique.add(i)
print(sum(Unique.difference(Duplicate)))