a = (int(x) for x in input("Nhập danh sách số : ").split())
s = 0
for i in a:
    if i % 2 == 0:
        s += i
print("Tổng các số chẵn là :", s)
