# Bài 00: Viết chương trình tính tích các phần tử trong một dict

my_dict = {
    '1' : 1,
    '2': "zx",
    '3' : 3
}
mul = 1
count = 0
for i in my_dict :
    if (type(my_dict[i]) is not int)  :
        if type(my_dict[i]) is str :
                count +=1
        else:
            count = 1
            break;
    if count > 1 :
        count = 3
        break;
    mul *= my_dict[i]
if count == 3 :
    print('Error!')
else :
    print(mul)




