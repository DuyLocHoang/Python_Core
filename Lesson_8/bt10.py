
# Bài 10: Kết quả của đoạn chương trình sau là gì?
#     try:
#         print("throw")
#     except:
#         print("except")
#     finally:
#         print("finally")

try:
    print("throw")
except:
    print("except")
finally:
    print("finally")

Output: 
throw
finally
Diễn giải : Cố gắng thực hiện đoạn code print throw. Nếu có lỗi print except. Dù sai hay đúng vẫn phải print finally