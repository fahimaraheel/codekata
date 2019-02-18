number = int(raw_input())
exponent = int(raw_input())
power = 1
for i in range(1, exponent + 1):
    power = power * number
print(power)
