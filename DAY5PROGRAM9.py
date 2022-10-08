l1=[]
l2=[]

ele1=int(input("ENTER THE NUMBER OF ELEMENTS OF 11: "))
print("ENTER THE ELEMENTS: ")
for i in range(0,ele1):
    val=int(input())
    l1.append(val)

ele2=int(input("ENTER THE NUMBER OF ELEMENTS OF 12: "))
print("ENTER THE ELEMENTS: ")
for i in range(0,ele2):
    val=int(input())
    l2.append(val)

l3=[]
# minx=min(ele1,ele2)
# sum_len=minx+(max(ele1,ele2)-minx)

for i in range(0,max(ele2,ele1)):
    if i<min(ele2,ele1):
        l3.append(l1[i])
        l3.append(l2[i])
    else:
        if ele2>ele1:
            l3.append(l2[i])
        if ele1<ele2:
            l3.append(l2[i])

print("Shuffled list: ",l3)
