# 1. Nhập vào 2 số nguyên a, b. In ra các số nguyên nằm giữa a và b trên cùng 1 dòng.

#---------------------
a = int(input("Nhap so nguyen a : "))
b = int(input("Nhap so nguyen b : "))

for i in range(b+1,a,1 ) :
    print(i ,end = ' ')
#-----------------------