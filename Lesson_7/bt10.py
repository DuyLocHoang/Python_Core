# Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
#         Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)



def dem(n) :
    if n == 0 :
        return 0
    else :
        if (n%10)%2 != 0 :
            return 1 + dem(int(n/10))
        else :
            return dem(int(n/10))
n = -1
while(n < 0) :
    n = int(input('Nhap so nguyen duong : '))
print(dem(n))
