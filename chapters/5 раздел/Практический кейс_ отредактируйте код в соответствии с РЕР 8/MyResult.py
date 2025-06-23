# Запрашиваем коэффиценты.
coff_one = int(input("coff_one = "))
coff_two = int(input("coff_two = "))
coff_three = int(input("coff_three = "))
discriminant = (coff_two**2) - (4 * coff_one * coff_three)

print()

# Решение по общей формуле.
x_one = ((-coff_two) + discriminant**0.5) / 2
x_two = ((-coff_two) - discriminant**0.5) / 2

print(f"Root one: {x_one}")
print(f"Root two: {x_two}")
