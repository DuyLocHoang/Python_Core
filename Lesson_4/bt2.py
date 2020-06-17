my_list = [0, 1, 2, 3, 8, 5, 6, 7, 8, 9]
tong = 0
tich = 1

for i in range(len(my_list)) :
    tong += my_list[i]
    tich *=my_list[i]
print(tong)
print(tich)
