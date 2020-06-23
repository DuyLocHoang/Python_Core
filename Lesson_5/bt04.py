# Bài 04: Cho 1 list chứa các tuple không rỗng.
#     Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
#     Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]
my_list = [(1,2,3,4),(4,3,2,2),(1,1),(3,3)]
for i in range(len(my_list)) :
    for j in range(len(my_list)) :
        if my_list[i][-1] < my_list[j][-1] :
            tg = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = tg
print(my_list)