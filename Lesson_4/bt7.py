#  Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.
list1 = [0,1,2,3,4,5]
list2 = [8,8,8,8]
a = 0
for i in range(len(list1)) :
        if list1[i] in list2 :
            a = 1
if a == 1 :
    print('List 1 va List 2 co chung phan tu')
else :
    print('List 1 va List 2 ko co chung phan tu')     
