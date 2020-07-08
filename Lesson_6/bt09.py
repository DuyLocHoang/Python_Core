# Bài 09: Viết hàm đếm số lần xuất hiện các ký tự trong một String
# Ví dụ:
#     Input: ‘Stringings’
#     Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}
s = 'Stringings'
my_dict = {i : s.count(i) for i in s}
print(my_dict)

