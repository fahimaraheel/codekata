print("QUEUE DATA STRUCTURE")
queue=[]
while True:
    print("what function do you want to perform?\n 1.insert an element,2.delete an element,3.length of the element,4.emptiness,5.exit")
    choice=int(input())
    if choice==1:
       print("enter the element you want to insert:")
       l = input()
       queue.append(l)
       print("the elements in queue are:",queue)
    elif choice==2:
       if queue==[]:
          print("Empty queue .You cannot delete!!")
       else:
          queue.pop(0)
          print("The elements in the queue are:",queue)
    elif choice==3:
        print("size of the queue is:",len(queue))
    elif choice==4:
       if queue==[]:
          print("Your queue is empty!!")
       else:
          print("You have",len(queue),"elements in your queue")
    elif choice==5:
          print("Exit")
          break
    
