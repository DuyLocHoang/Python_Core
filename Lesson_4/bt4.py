# Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.
my_list = [0, 1, 2, 3, 8, 5, 6, 7, 8, 9]
m = int(input("NHap m = "))
list1 = my_list[ : m]
list2 = my_list[m :]
print(list1)
print(list2) 