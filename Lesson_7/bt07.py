# Bài 07: Viết hàm
#         def create_matrix(n, m)
#     xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j
import numpy as np
def create_matrix(n,m) :
    big_list = []
    for i in range(n) :
        small_list = []
        for j in range(m) :
            small_list.append(i*j)
        big_list.append(small_list)
    print(np.array(big_list))

create_matrix(5,6)