# Bài 06: Viết chương trình tạp ra 26 file text có tên lần lượt từ A.txt, B.txt đến Z.txt
print(chr(65))
def mkfile():
    i = 65
    while( i <= 90) :
        data = f'text/text{chr(i)}.txt'
        with open(data,'w',encoding='utf-8') as f :
            f.write('')
        i+=1
mkfile()
