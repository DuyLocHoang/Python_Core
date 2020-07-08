# Bài 08: Viết hàm
#         def body_mass_index(m, h)
#     để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
#       Viết hàm
#         def bmi_information(m, h)
#     để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
m = float(input('Can nang (kg) : '))
h = float (input('Chieu cao (m) : '))
body_mass_index = lambda m,h : m / (h*h)
print(body_mass_index(m,h))

def bmi_information(m,h) :
    ss = body_mass_index(m,h)
    if ss < 18.5 :
        print('Duoi chuan')
    elif  18.5 <= ss < 24.9 :
        print('Binh thuong')
    elif  25 <= ss < 29.9 :
        print('Thua can')
    elif  30 <= ss < 34.9 :
        print('Beo phi cap do I')
    elif  35 <= ss < 39.9 :
        print('Beo phi cap do II')
    else :
        print('Beo phi cap do III')    
        
bmi_information(m,h)