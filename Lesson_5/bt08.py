# Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
a = ((1,2,3,4),(1,2,3,4),1,2,3)
min = a[0]
for i in range(len(a)) :
    if min == a[i] :
        min = a[i]
    else :
        print("Tat ca phan tu khong giong nhau")
        break;
if min == a[-1] :
    print("Tat ca phan tu giong nhau")