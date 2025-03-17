from decimal import Decimal, getcontext

# getcontext().prec = 4
# print(Decimal(0.1) + Decimal(0.2) == Decimal(0.3))
# print(Decimal(0.1) + Decimal(0.2))
# print(Decimal("0.1") + Decimal('0.2'))

# getcontext().prec = 6
# print(Decimal("1") / Decimal("7"))

# getcontext().prec = 8
# print(Decimal("1") / Decimal("7"))

import decimal
 
number = Decimal("1.45")

# Округлення за замовчуванням до одного десяткового знаку
print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))

# Округлення вверх при нічиї (ROUND_HALF_UP)
print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP))

# Округлення вниз (ROUND_FLOOR)
print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR))

# Округлення вверх (ROUND_CEILING)
print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING))

print("Custom", number.quantize(Decimal("0.00000"), rounding=decimal.ROUND_HALF_UP))

# Округлення до трьох десяткових знаків за замовчуванням
print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal("0.000")))
