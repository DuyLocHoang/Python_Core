# Bài 04: Viết hàm
#         def is_prime(n)
#     để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
def is_prime(n) :
    if n == 1 :
        return False
    run = int(n/2 + 1)
    count = 0
    for i in range(1,run) :
        if n % i == 0 :
            count +=1
    if count > 2 :
        return False
    else :
        return True
print(is_prime(2))