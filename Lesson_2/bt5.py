# PyCore-Course / source /lesson_02/BaiTap02.png

import math
# -------------------------
n = int(input("Nhap vao so nguyen duong n = "))
x = int(input("Nhap vao so thuc x = "))
# --------------------------
S1 = 0
for i in range(n+1) :
    S1 += x ** i
print("S1 = " + str(S1))
# ------------------------
S2 = 0
for i in range(n+1) :
    if i % 2 == 0 :
        S2 += x ** i
    else :
        S2 -= x ** i
print("S2 = " + str(S2))
# --------------------------
S3 = 1
fac = 1
for i in range(1,n+1) :
    fac *= i
    S3  += (x ** i)/fac
print("S3 = " +str(S3))
 


