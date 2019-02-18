inp=raw_input().split()
N=int(inp[0])
k=int(inp[1])
power = 1
for i in range(1, k + 1):
    power = power * N
print(power)
