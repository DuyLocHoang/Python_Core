# Bài 03: Viết chương trình trộn 2 file thành file mới
def merge_files() :
    with open('text/text.txt','r',encoding='utf-8') as text :
        data1 = text.read()
    with open('text/text2.txt','r',encoding='utf-8') as text2 :
        data2 = text2.read()
    with open('text/text3.txt','w',encoding='utf-8') as text3 :
        text3.write(data1+data2)
merge_files()