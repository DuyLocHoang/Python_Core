# Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
sen = input("Nhap cau: ")
sen.strip()
seperate= sen.split()
max = 0
for i in range(len(seperate)) :
    if max < len(seperate[i]) :
        max = len(seperate[i])
        count = i
print(f"Tu dai nhat trong cau  : {seperate[count]}")
