# Bài 05: Viết hàm
#         def count_upper_lower(str)
#     trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
s = input('Nhap chuoi: ')
def count_upper_lower(a) :
    count_upper = 0
    count_lower = 0
    for i in s :
        if 'A'<= i <='Z' :
            count_upper +=1
        if 'a' <= i <= 'z' :
            count_lower +=1 
    print(f'So chu cai viet hoa {count_upper}')
    print(f'So chu cai viet thuong {count_lower}')
count_upper_lower(s)