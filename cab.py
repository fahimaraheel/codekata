place=["tambaram","adayar","ambattur"]
dist=[35,30,50]
price=[5,8,10]
print("WHERE YOU WANT TO GO?\n 1.tambaram,2.adayar,3.ambattur")
choice=int(input())
if choice==1:
    kms=dist[0]
    print("The place you have choosed is tambaram")
elif choice==2:
    kms=dist[1]
    print("The place you have choosed is adayar")
elif choice==3:
    kms=dist[2]
    print("The place you have choosed is ambattur")
print("WHICH DO YOU PREFER?\n 1.nano,2.micro,3.prime")
option=int(input())
if option==1:
    rup=price[0]
    print("The cab you have choosed is nano")
elif option==2:
    rup=price[1]
    print("The cab you have choosed is micro")
elif option==3:
    rup=price[2]
    print("The cab you have choosed is prime")
print ("the estimated amount is",kms*rup)
print("Do you want to confirm your booking?\n 1.yes,2.no")
choice=int(input())
if choice==1:
      print("Thank you for your booking")
elif choice==2:
      print("better luck next time")
