l=(input("Nhập vào danh sách các số ")).split()
u=sorted(set(l), key=l.index)
print("Danh sách không bị lặp là : ", u)
