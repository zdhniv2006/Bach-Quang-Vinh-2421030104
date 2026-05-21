n = int(input("nhập n="))
đếm = 0
i = 2
while n > 1:
    if n % i != 0:
        i = i + 1
    else:
        đếm = đếm + 1
        while n % i == 0:
            n = n // i

print()
print("số các số nguyên tố là:", đếm)
