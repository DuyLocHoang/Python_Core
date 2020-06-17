# Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
chuoi = input("Nhap chuoi :")
my_list = [1,2,3]
your_list = []
for i in my_list :
    your_list.append(str(i)+chuoi) 
print(your_list)
