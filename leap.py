cd=int(raw_input())
if((cd%400==0) or ((cd%4==0) and (cd%100!=0))):
    print("yes")
else:
    print("no")
