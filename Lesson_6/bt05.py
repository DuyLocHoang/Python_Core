# Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
#         Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
a = int(input('so phan tu :'))
b = int(input('So phan tu trong value: '))
import random as rd
my_list1 = []
my_list2 = []
for i in range(a) :
    my_list1.append(rd.randint(i,10))
for i in range(b) :
    my_list2.append(rd.randint(i,10))
my_dict = {}.fromkeys(my_list1,my_list2)
print(my_dict)
value = list(my_dict.items())
for i in range(len(value)) :
    print(value[i][1][4])


