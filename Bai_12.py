numb=input("Nhập vào một chuỗi số : ").split()
print("Phần tử xuất hiện nhiều nhất là : ", max(set(numb), key=numb.count))
print("Số lần xuất hiện của phần tử đó là : ", numb.count(max(set(numb), key=numb.count)))