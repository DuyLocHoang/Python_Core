# Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.
my_list = [(1,2,3,4),(4,3,2,2),(1,1),(3,3),(0,0)]
min = my_list[0][1]
for i in range(len(my_list)) :
    if min > my_list[i][1] :
        min = my_list[i][1]
        count = i
print(my_list[count])