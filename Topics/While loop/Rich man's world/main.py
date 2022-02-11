PROTECTED = 700000
INTEREST = 7.1 / 100

year = 0
value = float(input())

while value < PROTECTED:
    value += (INTEREST * value)
    year += 1

print(year)
