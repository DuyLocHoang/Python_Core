# Bài 07: Đoạn chương trình sau in ra gì?
#     number = 5.0
#     try:
#         r = 10/number
#         print(r)
#     except:
#         print("Oops! Error occurred.")
number = 5.0
try:
    r = 10/number
    print(r)
except:
    print("Oops! Error occurred.")

Output : 2.0
Diễn giải :Cố gắng thực hiện 10/number . Nếu có lỗi in ra Oops! Error occurred.