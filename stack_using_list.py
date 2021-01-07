stack=[]
def push():
    element = input("enter the element")
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop_element()
        print("removed element".e)
        print(stack)
while True:
    print("select the operation \n 1.push\n 2.Pop\n 3.quit")
    choice=int(input())
    if(choice==1):
        push()
    elif(choice==2):
        pop_element()
    elif(choice==3):
        break
    else:
        print("enter a valid choice")