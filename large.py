InputValue=raw_input() 
e,f,g=InputValue.split(" ")
if((e>f) and (e>g)):
    print(e)
elif((f>e) and (f>g)):
    print(f)
elif((g>e) and (g>f)):
    print(g)
