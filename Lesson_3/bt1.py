# Bài 01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.

s = input("Nhap chuoi : ")
a =s[1:]
a = a.replace(s[0],"$")
s_new = s[0] + a
print(s_new)
