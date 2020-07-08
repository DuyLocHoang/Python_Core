# Bài 06: Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple.
my_list = (1,2,2+3j)
if len(my_list) < 4  :
    print("Error!")
else :
    print(my_list[3])
    print(my_list[-4])