# PyCore-Course / source /lesson_02/BaiTap03.png
n = float(input("Nhap vao so nguyen duong bat ky <1000 n = "))

while (n-int(n)) != 0 or n > 1000 or n < 0 :
    print("Dau vao Sai!")
    n = float(input("Nhap vao so nguyen duong bat ky <1000 n = "))
n =int(n)
tong = 0
while (n != 0) :
    tong += n % 10
    n //=10
print("Tong = " + str(tong))