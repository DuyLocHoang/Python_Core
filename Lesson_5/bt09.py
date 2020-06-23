# Bài 09: Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.
a = (1,2,3,4,5)
tong = 0
max =a[0]
for i in range(len(a)) :
    tong += a[i]
    if max < a[i] :
        max = a[i]
print(tong)
print(max)