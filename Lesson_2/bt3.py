# 3. Nhập vào số tự nhiên n, tính tổng các số chia hết cho 3 mà nhỏ hơn n

# ------------------------------------------
n = int(input("Nhap vao so tu nhien n : "))
tong = 0

for i in range(0,n,3) :
    tong += i
print("Tong = " + str(tong))
# ----------------------------------------------