# Bài 02: Viết chương trình đảo ngược một tuple.
a = (1,2,3,4,[1,2,3,4])
rv1 = list(a)
rv = reversed(a)
cvt = tuple(rv)
print(cvt)