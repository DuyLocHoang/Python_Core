# Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
#             F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
#     Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
#         + Hàm Đệ quy
#         + Hàm Không đệ quy
#Hàm đệ quy
# def fibo(n) :
#     if n < 3 :
#         return 1
#     elif n == 3 :
#         return 2
#     else :
#         return fibo(n-1) + fibo(n-2) + fibo(n-3)
# print(fibo(5))
#Hàm không đệ quy
def no_fibo(n):
    if n < 3 :
        return 1
    elif n == 3 :
        return 2 
    i = 4 
    a = 0
    a1 = a2 = 1 
    a3 =2 
    while(i <= n) :
        a = a1 + a2 + a3
        a1 = a2
        a2 = a3
        a3 = a
        i+=1
    return a
print(no_fibo(5))