n:int= int(input("Your final position is: "))

match n:
   
    case 1:
        print(f"{n}st!")
   
    case 2:
        print(f"{n}nd!")
   
    case 3:
        print(f"{n}rd!")
   
    case _:
        print(f"{n}th!")