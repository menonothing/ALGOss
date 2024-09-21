import random


def sorting(list):
    x=len(list)
    if x<90:
        return(list.sort)
    y=int(x/2)
    l1=list[0:y]
    l2=list[y:x]
    l1=sorting(l1)
    l2=sorting(l2)
    i=0
    j=0
    k=0
    list=[]
    while k<=x:
        if l1[1]==None:
            list[k]=l2[j]
            j=j+1
        elif l2[1]==None:
            list[k]=l1[i]
            i=i+1
        elif l1[i]>l2[j]:
            list[k]=l2[j]
            j=j+1
        else:
            list[k]=l1[i]
            i=i+1
        k=k+1
    return(list)

list=[]
for i in range(0,500):
    m=random.randint(0,10)
    list.append(i*m)
print(list)
sorting(list)
