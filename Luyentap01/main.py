#This i =========================
# BÀI 1
# =========================
print("===== BÀI 1 =====")

# Tạo các biến
so_nguyen = 10
so_thuc = 5.5
chuoi = "Hello Python"

# In ra màn hình
print("Số nguyên:", so_nguyen)
print("Số thực:", so_thuc)
print("Chuỗi:", chuoi)


# =========================
# BÀI 2
# =========================
print("\n===== BÀI 2 =====")

# Khai báo hằng số PI và bán kính
PI = 3.14
r = 5

# Tính chu vi hình tròn
chu_vi = 2 * PI * r

# In kết quả
print("Chu vi hình tròn là:", chu_vi)


# =========================
# BÀI 3
# =========================
print("\n===== BÀI 3 =====")

# Nhập hai số nguyên từ bàn phím
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

# Tính toán
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
# In kết quả
print("Tổng =", tong)
print("Hiệu =", hieu)
print("Tích =", tich)
print("Thương =", thuong)
# =========================
# BÀI 4
# =========================
print("\n===== BÀI 4 =====")

# Định nghĩa hàm
def sum_two_numbers(a, b):
    return a + b

# Gọi hàm
ket_qua = sum_two_numbers(7, 3)

# In kết quả
print("Tổng hai số là:", ket_qua)


# =========================
# BÀI 5
# =========================
print("\n===== BÀI 5 =====")

# Khai báo biến
name = "Dat"
age = 19
average_score = 8.5

# Hiển thị kiểu dữ liệu
print("Kiểu dữ liệu của name:", type(name))
print("Kiểu dữ liệu của age:", type(age))
print("Kiểu dữ liệu của average_score:", type(average_score))

# Xử lý dữ liệu
age_next_year = age + 1
doubled_score = average_score * 2

#In thông tin
print("Tên:", name)
print("Tuổi hiện tại:", age)
print("Tuổi năm sau:", age_next_year)
print("Điểm trung bình:", average_score)
print("Điểm gấp đôi:", doubled_score)
