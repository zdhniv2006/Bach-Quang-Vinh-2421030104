a = int(input("Nhập số nguyên dương a: "))
tich_chu_so = 1
temp = a
while temp > 0:
    tich_chu_so *= temp % 10
    temp //= 10
if tich_chu_so % 2 == 0 and tich_chu_so > 20:
    print(f"Tích các chữ số = {tich_chu_so} → Là số chẵn và lớn hơn 20.")
else:
    print(f"Tích các chữ số = {tich_chu_so} → Không thỏa mãn.")
