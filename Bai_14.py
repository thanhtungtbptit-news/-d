numb = input("Nhập vào một chuỗi số : ").split()
numb = [int(x) for x in numb]
numb_10 =[x for x in numb if x > 10]
print("Danh sách các số lớn hơn 10 là : ",numb_10)