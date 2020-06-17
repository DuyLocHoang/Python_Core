list1 = [0,1,2,3,4,5]
list2 = [8,8,8,8]
a = 0
for i in range(len(list1)) :
    for j in range(len(list2)) :
        if list1[i] == list2[j] :
            a = 1
if a == 1 :
    print('List 1 va List 2 co chung phan tu')
else :
    print('List 1 va List 2 ko co chung phan tu')     
#a = [1 for i in range(len(list1)) for j in range(len(list2)) if list1[i] == list2[j]]
