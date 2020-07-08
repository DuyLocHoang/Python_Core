# Bài 02: Viết hàm
#         def reverse_string(str)
#     trả lại chuỗi đảo ngược của chuỗi str

def reverse_string(a) :
    st = ''
    for i in a :
        st = i + st
    return st
s = input('Nhap chuoi: ')
print(reverse_string(s))
