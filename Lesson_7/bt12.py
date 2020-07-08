# Bài 12: Viết hàm
#         def find_x(a_list, x)
#     trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1

a_list = [1,1,1,2,5]
def find_x(a_list,x) :
    my_list = []
    for i in range(len(a_list)) :
        if x == a_list[i] :
            my_list.append(i)
    if my_list == [] :
        return -1
    else :
        return my_list      

print(f'Vi tri tri x xuat hien {find_x(a_list,2)}') 