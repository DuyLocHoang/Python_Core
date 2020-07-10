# Bài 01: Viết hàm
#         def max_min(*numbers)
#     trả lại cả giá trị max, min của nhiều số được truyền vào

# def max(a,b) :
#     max = a
#     if a < b :
#         max = b
#     return max
# def min(a,b) :
#     min = a
#     if a > b :
#         min = b
#     return min
# def max_min(a,b,c):
#     print(f'max = {max(a,max(b,c))}')
#     print(f'min = {min(a,min(b,c))}') 

# max_min(5,9,7)

def max_min(*numbers):
    my_list = [max(numbers),min(numbers)]
    return my_list

print(f'max : {max_min(1,2,3,45)[0]} \nmin : {max_min(1,2,3,45)[1]}')
