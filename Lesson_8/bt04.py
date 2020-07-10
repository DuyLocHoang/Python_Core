# Bài 04: Viết hàm
#         def get_file_size(file)
#     để lấy và trả về dung lượng của file
def get_file_size(file) :
    with open(file,'r',encoding='utf-8') as text :
        text.read()
        print(text.tell())

get_file_size('text/text.txt')
