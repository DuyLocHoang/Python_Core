# Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict
my_dict = {
    1 : 'x',
    3: 2,
    2 : 1,
    6 : 2
}

my_dict = sorted(my_dict.items() )
print(f"{my_dict[-1]}")
print(f"{my_dict[-2]}")
print(f"{my_dict[-3]}")
