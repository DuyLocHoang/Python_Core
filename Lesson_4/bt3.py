# Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.
y_list = [0, 1, 2, 3, 8, 5, 6, 7, 8, 9]
max = min = my_list[0]
for i in range(len(my_list)) :
    if max < my_list[i] :
        max = my_list[i]
    if min > my_list[i] :
        min = my_list[i]
print(max)
print(min)


