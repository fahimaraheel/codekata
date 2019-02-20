inp=raw_input().split()
low=int(inp[0])
up=int(inp[1])
for num in range(low+1,up):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp % 10
        sum += digit ** order
        temp //=10
    if num == sum:
        print num,
