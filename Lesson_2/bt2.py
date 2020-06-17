# 2. Nhập vào số tự nhiên n, rồi tính giai thừa của n (ko dùng factorial của math)

#------------------------------------------
n = int(input("Nhap vao so tu nhien n : "))
fac = 1

for i in range(1,n+1) :
    fac *=i
print('{0}! = {1}'.format(n,fac))
#--------------------------------------------
