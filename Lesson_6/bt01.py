# Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict
my_dict = {
    '1' : 1,
    '2': 2,
    '3' : 3
}
func = lambda x: x[0]
my_dict = sorted(my_dict.items(), key =func )
print(f'min is : {my_dict[0][0]}' )
print(f'max is: {my_dict[-1][-1]}')