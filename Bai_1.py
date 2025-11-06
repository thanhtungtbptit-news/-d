text= input("Nhập vào một chuỗi ký tự: ")
print("Độ dài chuỗi ký tự đã nhập là: ", len(text))
print("Số lần xuất hiện mỗi kí tự trong chuỗi là : ", {char: text.count(char) for char in set(text)})