inp=raw_input().split()
start = int(inp[0])
ender = int(inp[1])
for num in range(start+1,ender):
    if num>1:
        for i in range (2,num):
            if (num%i)==0:
                break
        else:
            print num,
