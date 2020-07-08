# Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
# Ví dụ:
#     Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#     Output: {'item1': 1150, 'item2': 300}
my_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
my_dict = {}
for i in my_list :
    value = list(i.values())
    if value[0] in my_dict :
        value[1] += my_dict[value[0]]
    my_dict.update({
        value[0] :value[1]
    })
print(my_dict)