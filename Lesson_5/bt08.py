# Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
a = (1,1,1,1,2)
# min = a[0]
# for i in range(len(a)) :
#     if min == a[i] :
#         min = a[i]
#     else :
#         print("Tat ca phan tu khong giong nhau")
#         break;
# if min == a[-1] :
#     print("Tat ca phan tu giong nhau")
# Bài bt08: có thể dùng hàm count hoặc có thể dùng set nhé! thử 2 cái này xem sao
# Count
# count = a.count(a[0])
# if count == len(a) :
#     print('Tat ca phan tu giong nhau')
# else :
#     print("Tat ca phan tu ko giong nhau")

#Set
re_a = set(a)
if len(re_a) == 1 :
    print('Tat ca phan tu giong nhau')
else :
    print('Tat ca phan tu ko giong nhau')
