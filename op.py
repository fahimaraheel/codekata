print("STACK DATA STRUCTURE")
stack=[]
while True:
    print("what function do you want to perform?\n 1.insert an element,2.delete an element,3.length of the element,4.emptiness,5.exit")
    choice=int(input())
    if choice==1:
       print("enter the element you want to insert:")
       l = input()
       stack.append(l)
       print("the elements in stack are:",stack)
    elif choice==2:
       if stack==[]:
          print("Empty stack .You cannot delete!!")
       else:
          stack.pop()
          print("The elements in the stack are:",stack)
    elif choice==3:
        print("size of the stack is:",len(stack))
    elif choice==4:
       if stack==[]:
          print("Your stack is empty!!")
       else:
          print("You have",len(stack),"elements in your stack")
    elif choice==5:
          print("Exit")
          break
    
