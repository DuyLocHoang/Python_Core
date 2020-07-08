# Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict
my_dict = {
    1 : 'x',
    3: 2,
    2 : 1,
    6 : 2,
    3: 'x'
}
re_dict = set(my_dict.values())
print(re_dict)

