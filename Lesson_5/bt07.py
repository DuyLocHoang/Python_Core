# Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
a = (1,2,3,4)
a_1 = set(a)
b = (5,6,7,8)
b_1 = set(b)
if a_1.isdisjoint(b_1)  :
    print("Ko Giao")
else :
    print("Co giao")