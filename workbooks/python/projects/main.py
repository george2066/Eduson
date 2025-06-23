from time import monotonic

integers = [2, 3, 4, 5, 6, 7, 8, 9]

def plus_one(integer):
    return integer + 1

start = monotonic()
integers = map(plus_one, integers)
diff = monotonic() - start
print(f"d = {diff:0.20f}")

start = monotonic()
integers = plus_one(5)
diff2 = monotonic() - start
print(f"d = {diff2:0.20f}")