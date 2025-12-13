stop = True

while stop:
    num = int(input("Please choose number 1,2,3"))
    if(num==1):
         print("Your number is one")
    elif(num==2):                               
        print("Your number is two")
    elif(num==3):
        print("Your number is three")
    elif(num==4):
        print("No 4 stupid")
        stop = False
    else:
        print("Invalid input")