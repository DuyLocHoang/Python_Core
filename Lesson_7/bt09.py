# Bài 09: Viết hàm
#         def change_upper_lower(str)
#     chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str

s = input("Nhap chuoi :")
def change_upper_lower(s) :
    a =""
    for i in s :
        if i == i.lower() :
            a += i.upper()
        else :
            a += i.lower()
    print(a)
change_upper_lower(s)