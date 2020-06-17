# Bài 08: Cho list các số nguyên dương A.
#        Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.
list2 = [2,1]
list1 = [8,8,8,8]
a = 0
for i in range(len(list1)) :
    for j in range(i+1,len(list2)) :
        if list1[i] > list2[j] :
            a +=1
print(a)