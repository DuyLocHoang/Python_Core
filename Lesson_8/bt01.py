# Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng
try :
    a = int(input("Lines: "))
except ValueError :
    print('Nhap sai ')

def read_lines(a) :
    with open("text/text.txt",'r',encoding='utf-8') as text :
        for i in range(a) :
            print(text.readline(-1))
    
read_lines(a)
