inp=raw_input().split()
start = int(inp[0])
ender = int(inp[1])
for num in range(start+1,ender):
    if num%2 == 0:
        print num,
