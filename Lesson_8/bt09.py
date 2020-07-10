# Bài 09: Kết quả output của đoạn chương trình sau là gì?
#     def hoan_function():
#         try:
#             print('Monday')
#         finally:
#             print('Sunday')
#     hoan_function()
def hoan_function():
    try:
        print('Monday')
    finally:
        print('Sunday')
hoan_function()
Output:
Monday
Sunday

Diễn giải : Cố gắng thực hiện đoạn code print Monday. Dù đúng hay sai đều phải thực hiện print Sunday