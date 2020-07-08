# Bài 06: Viết hàm
#         def is_pangram(str, alphabet)
#     đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
#     Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần
s = input('Nhap chuoi :')
alphabel = input('alphabel : ')
s = s.lower()
alphabel =alphabel.lower()
is_pangram = lambda s,alphabel : True if set(alphabel) - set(s) == set() else False
print(is_pangram(s,alphabel))