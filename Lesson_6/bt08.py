# Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict
my_dict = {
    '1' : 1,
    '2': 2,
    '3' : 3,
    '4' :4
}
func = lambda x: x[0]
my_dict = sorted(my_dict.items(), key =func, reverse=True )
mylist = []
for i in range(3) :
    mylist.append(my_dict[i])
print(dict(mylist))