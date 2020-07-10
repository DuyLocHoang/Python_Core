# Bài 02: Viết chương trình thêm một chuỗi nào đó vào cuối file
s = input('Nhap chuoi: ')
def add_str(s) :
    with open('text/text.txt', 'a',encoding='utf-8') as text :
        print(text.write(s))
add_str(s)
