menu=["1. Show the even numbers from x to y" ,"2. Show the odd numbers from x to y " ,"3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)" , "4. Exit the program"]
x=int(input("Enter first number:"))
y=int(input("Enter ending number:"))
print(menu)
choice=int(input("choice="))
while choice!=4:
    if choice==1:
        for i in range( x , y+1):
            if i %2==0:
                print(i)
        choice = int(input("choice="))

    elif choice==2:
        for i in range(x,y+1):
            if i %2!=0:
                print(i)
        choice = int(input("choice="))

    elif choice==3:
        for i in range(x,y+1):
            print(i*i)
        choice = int(input("choice="))

    else:
        print("Invalid!")
        choice=int(input("choice="))
print("Thank you!")
