a = float(input("Nhap a : "))
b = float(input("Nhap b : "))
c = float(input("Nhap c : "))
if a+b>c or a+c>b or b+c>a :
    if( a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2 ):
        print("Tam giac vuong ")
    else :
        print("Tam giac thuong")
else :
    print("khong phai la 3 canh cua 1 tam giac")