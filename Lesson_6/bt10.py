# Bài 10: Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản
text = "Đoàn thuyền chở các bà các chị từ chợ huyện chợ tỉnh về cập bến Các bà các chị được đàn con ùa ra đón"
re_text = text.split(' ')
my_dict = {i : text.count(i) for i in re_text}
print(my_dict)