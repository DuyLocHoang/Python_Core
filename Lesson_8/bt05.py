# Bài 05: Viết hàm
#         def extract_characters(*file)
#     trả lại tập các ký tự trong các file
def extract_characters(*file) :
    for i in range(len(file)):
        data = file[i]
        print(data)
        with open(data , 'r',encoding= 'utf-8') as text :
            data = text.read()
            print(set(data))

extract_characters('text/text.txt','text/text2.txt','text/text3.txt') 