s = input("Nhap chuoi :")
min = max = s[0]

for i in range(len(s)) :
    if max < s[i] :
        max = s[i]
    if min > s[i] :
        min = s[i]
print(max)
print(min)