# Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
#     Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
my_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
my_tuple = []
for i  in range(len(my_list)) :
    a = (my_list[i][-3:-1]+ my_list[i][-1])
    if a == '.vn' :
        a = 'vn'
    my_tuple.append(a)
my_tuple = tuple(my_tuple)
print(my_tuple)
        
