s = input("Nhap chuoi :")
a =""
for i in range(len(s)) :
    if s[i] == s[i].lower() :
        a += s[i].upper()
    else :
        a += s[i].lower()
print(a)