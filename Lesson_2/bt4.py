""" Lập chương trình thực hiện công việc sau :
1. nhập 3 số a,b,c bất kì từ bàn phím
2. Giải và biện luận pt bậc 2
3. Đưa kq ra màn hình

"""
# ---------------------------------------------------------
import cmath
import math
a = float(input("Nhap a : "))
b = float(input("Nhap b : "))
c = float(input("Nhap c : "))

print("Ta co \n{}*x^2 + {}*x + {} = 0".format(a,b,c))

if a == 0 :
    print("Pt co 1 nghiem = " + str(round(-c/b,2)))
else :
    delta = b**2 - 4*a*c
    if delta == 0 :
        print("Pt co Nghiem kep : x1 = x2 =  " +str(round(-b/(2*a),2)) )
    else :

        if delta < 0 :
            x1 = (-b + cmath.sqrt(delta))/(2*a)
            x2 = (-b - cmath.sqrt(delta))/(2*a)
            print("Pt co 2 nghiem phan biet \nx1 = {} \nx2= {}".format(x1,x2))
        else :
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print("Pt co 2 nghiem phan biet \nx1 = {} \nx2= {}".format(x1,x2))
# --------------------------------------------------------------------------------