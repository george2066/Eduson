# Запрашиваем коэффиценты.
coff_one = int(input("coff_one = "))
coff_two = int(input("coff_two = "))
coff_three = int(input("coff_three = "))
discriminant = 0

print()

# Решение по сокращенной формуле, потому что второй коэффицент чётный.
if coff_one != 0 and coff_two % 2 == 0 and coff_three != 0:
    root = coff_two / 2
    discriminant = root**2 - coff_one * coff_three
    root_one = (-root + discriminant**0.5) / coff_one
    root_two = (-root - discriminant**0.5) / coff_one
    print("Решение по сокращенной формуле, потому что второй коэффицент чётный.")
    print(f"root_one = {root_one}")
    print(f"root_two = {root_two}")

# Решение полного уравнения.
if coff_one != 0 and coff_two % 2 != 0 and coff_three != 0:
    discriminant = coff_two**2 - 4 * coff_one * coff_three

    if discriminant > 0:
        root_one = (-coff_two + discriminant**0.5) / (2 * coff_one)
        print(f"Дискриминант равен: {discriminant}")
        print(f"Дервый корень равен: {round(root_one, 2)}")
        root_two = (-coff_two - discriminant**0.5) / (2 * coff_one)
        print(f"Второй корень равен: {round(root_two, 2)}")

    elif discriminant < 0:
        print(f"Так как дискриминант меньше нуля и равен: {discriminant}")
        print("Действительных корней нет")
    else:
        root = -coff_two / (2 * coff_one)
        print(f"Уравнение имеет один корень: {root}")

        # Решение уравнения при coff_two = 0.
        if coff_one != 0 and coff_three != 0 and coff_two == 0:
            if (-coff_three / coff_one) >= 0:
                root_one = (-coff_three / coff_one) ** 0.5
                print(f"Первый корень равен: {root_one}")
                root_two = (-1) * ((-coff_three / coff_one) ** 0.5)
                print(f"Второй корень равен: {root_two}")
        if (-coff_three / coff_one) < 0:
            print(
                f" -coff_three / coff_one = : {-coff_three / coff_one}, т.е. < 0, поэтому действительных корней нет"
            )

# Решение уравнения при coff_three = 0.
if coff_one != 0 and coff_three == 0 and coff_two != 0:
    print(f"Корень уравнения равен либо нулю, либо {-coff_two / coff_one}")

# Решение уравнения при coff_two = 0 и coff_three = 0.
if coff_one != 0 and coff_two == 0 and coff_three == 0:
    print(f"Корни уравнения равны нулю, coff_one * x ** 2 = 0")
