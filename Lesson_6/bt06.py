# Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
dict1 = {
    1: 1,
    2 : 2,
    3 : 'Name',
    4:4
}
dict2 = {
    2: 1,
    1 : 2,
    3 : 'Name',
    4 :4
}
dict1 = list(dict1.items())
dict2 = list(dict2.items())
for  i in dict1 :
    if i in dict2 :
        print(i)

    
