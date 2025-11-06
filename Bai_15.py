text=input("Nhập vào một đoạn văn : ")
a=text.lower().split()
for ch in ".,!?":
    text = text.replace(ch, "")
b=sorted(set(a), key=a.count, reverse=True)
print("Danh sách từ sắp xếp theo tần suất giảm dần là : ", b)
for w in b:
    print("Số lần xuất hiện của ký tự '{}' là : {}".format(w, a.count(w)))