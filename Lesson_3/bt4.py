s = input('Nhap chuoi: ')
if len(s) > 2 :
    s_n = s[:2] + s[len(s)-2:]
else :
    s_n = ''
print(s_n)    
