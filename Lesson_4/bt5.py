my_list = [0,0,0,0, 1, 2, 3, 10, 9, 10, 9, 8, 9]
max = my_list.count(my_list[0])

for i in range(len(my_list)) :
    if my_list.count(my_list[i]) >= max :
        max = my_list.count(my_list[i])
        j = my_list[i]
print(j)

        