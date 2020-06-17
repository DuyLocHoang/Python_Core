my_list = ['DDDDDD','AAAAAAA','bbbbb','abaascs','a']
a = 0
for i in range(len(my_list)) :
    if (len(my_list[i]) > 1) and (my_list[i][0] == my_list[i][-1]) :
        a +=1 
print(a)

