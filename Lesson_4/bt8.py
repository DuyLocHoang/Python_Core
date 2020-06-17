list2 = [2,1]
list1 = [8,8,8,8]
a = 0
for i in range(len(list1)) :
    for j in range(len(list2)) :
        if list1[i] > list2[j] and i < j :
            a +=1
print(a)