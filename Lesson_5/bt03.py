# Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.
my_list = [1,2,3,4, (5,6,7),6,7]
my_tuple = ()
count = 0
for i in my_list :
    if type(i) is tuple :
        break;
    count += 1
print(count) 