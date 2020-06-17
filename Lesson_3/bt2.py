s = input("Nhap chuoi : ")
while 1 :
    m = int(input("Nhap m = "))
    if m > 0 :
        break
s_n = s[:m] + s[m+1:] 
print(s_n)
        
    


