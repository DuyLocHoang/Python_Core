# Bài 02: Viết chương trình sắp xếp các phần tử của dict theo chiều tăng dần của key
my_dict = {
    1 : 'x',
    -1: 2,
    2 : 1,
    6 : 2
}
my_dict = sorted(my_dict.items() )
re_dict = dict(my_dict)
print(re_dict)