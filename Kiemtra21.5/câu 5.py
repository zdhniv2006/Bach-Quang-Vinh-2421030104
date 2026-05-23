a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
tong_chu_so_a = 0
temp = a
while temp > 0:
    tong_chu_so_n += temp % 10
    temp //= 10
print(f"Tổng các chữ số của a = {tong_chu_so_a}")
if tong_chu_so_a == 0:
    print("Tổng chữ số bằng 0, không thể chia het.")
elif m % tong_chu_so_a == 0:
    print(f"{b} chia hết cho {tong_chu_so_a}.")
else:
    print(f"{b} không chia hết cho {tong_chu_so_a}.")
