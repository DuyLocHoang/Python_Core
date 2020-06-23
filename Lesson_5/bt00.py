# Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
#     Sau đó, unpack các phần tử trong một tuple.
import random
import string
my_list = (random.sample(range(100),3),random.randint(1,10),tuple(random.sample(range(100),5)),random.choice(string.ascii_lowercase))
a,b,c,d = my_list
print(my_list)
print(f'a = {a}\nb = {b}\nc = {c}\nd = {d}')