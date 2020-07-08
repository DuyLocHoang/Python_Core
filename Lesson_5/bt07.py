# Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
a = (1,2,6,4)
b = (5,6,7,8)
# a_1 = set(a)
# b_1 = set(b)
# if a_1.isdisjoint(b_1)  :
#     print("Ko Giao")
# else :
#     print("Co giao")
count = 0
for i in a :
    if i in b :
        count = 1
        break
if count :
    print("Co phan tu chung")
else :
    print("Ko co phan tu chung")
