import statistics
import math


def hello(name):
    print(f"Hrllo, {name}!")


def area(length, width):
    print(f"Area equals (in metr): {length * width}")


def sum_digit(fourdigit):
    return (
        (fourdigit // 1000)
        + (fourdigit % 1000 // 100)
        + (fourdigit % 1000 % 100 // 10)
        + (fourdigit % 1000 % 100 % 10)
    )


def service(goods):
    return goods * 30 + 70


def mediana(*args):
    return statistics.median(args)


def count_second(*args):
    seconds1 = 0 + (args[1] * 3_600) + (args[2] * 60) + args[3]
    seconds2 = (args[4] * 86_400) + (args[5] * 3_600) + (args[6] * 60) + args[7]
    return seconds2 - seconds1 - 86_400


def renovation(length, width, area_plit, quantity_plit, **kwards):  # 100 3 3 o:12
    area = length * width
    quantity_plits = math.ceil(area / area_plit)
    quantity_pack = math.ceil(quantity_plits / quantity_plit)
    price = kwards[min(kwards, key=kwards.get)]
    return quantity_pack * price


def parity_check(day, area):
    if (day % 2 == 0 and area % 2 == 0) or (day % 2 == 1 and area % 2 == 1):
        return True
    else:
        return False


def stats(*args):
    avr = sum(args[:7]) / 7
    general = sum(args[:7])
    maximum = args[max(args)]
    minimum = args[min(args)]
    return f"Среднее время в день: {avr}, Всего времени: {general}, Максимальное время: {maximum}, Минимальное время: {minimum}."
