# #MADLIBS 

# adjective1 = input("enter a adjective ")
# noun1 = input("enter a noun")
# adjective2 = input("enter a adjective ")
# verb1 = input ("enter a verb")
# adjective3 = input("enter a adjective ")

# print(f"yesterday i went to a  {adjective1} zoo")
# print(f"in the exibit i saw {noun1}")
# print(f"{noun1}was {adjective2}and {verb1}")
# print(f"i was{adjective3}")

# import math 

# rad = float(input('enter your circles radius '))
# circ = 2 * math.pi * rad 
# print(f"circumfrence is {round(circ,2)}")

# area = math.pi* pow(rad,2)
# # print (f"area of the circle is {round(area,2)}")

# import math 
# a = float(input("enter the value of side a "))
# b = float(input("enter the value of side b "))

# c = math.sqrt(pow(a,2) + pow(b,2))
# print(f"the value of hypotneus is {round(c,2)}")

# print(f"please enter a number to start converting")
# print(f"1.miles to kilometre")
# print(f"2.kg to pounds")
# print(f"3.celsious to ferenheit")


# opt= int(input())
# if opt == 1:
#     print(f"miles to kilometre")
#     ml=float(input("enter the miles"))
#     result= ml* 1.60934
#     print(f"km value is {round(result,2)}")
# elif opt == 2:
#     print(f"kg to pounds")
#     kg = float(input("enter the kg "))
#     result = kg *  2.205
#     print (f"the converted pounds is {round(result,2)}")
# elif opt == 3:
#     print(f"celsious to ferenhiet")
#     c = float(input("enter the celcious value "))
#     result = (c*(9/5))+32
#     print(f"the converted fernhiet is {round(result,2)}f")
# else:
#     print("invalid option selected")
    

# user_ = input("enter your user name ")
# if len(user_) >=12 :
#     print("your user name cannot have more that 12 char")
# elif not user_.find(" ") == -1:
#     print("your user name cannot contain any spaces ")
# elif not user_.isalpha():
#     print("your user name cannot contain any numbers")
# else:
#     print(f"welcome {user_} your yearly femboy subscription is active it will be sent to the nearest anthropic server to train claude on femboy manners ")
    
    
# prnc= 0 
# intrest = 0 
# time = 0

# print("compond intrest calculator")

# while prnc <=0:
#     prnc = float(input("enter your principle amount "))
#     if prnc <=0:
#         print("principle amount cannot be less than or equal to 0")


# while intrest <=0:
#     intrest = float(input("enter your intrest rate "))
#     if intrest <=0:
#         print("intrest amount cannot be less than or equal to 0")

# while time <=0:
#     time = int(input("enter your time in years  "))
#     if time <=0:
#         print("time  cannot be less than or equal to 0")
        
# #amount calc 

# amount = prnc*pow((1+intrest/100),time)

# print(f"your total amount would be {amount}")


# #simple timer using for 

# import time 
# user_input = input("hours? ")
# if user_input == "n":
#     pass 
# else:
#     my_time += int(user_input) * 3600



# for i in range(my_time,0,-1):
#     seconds = int(i % 60)
#     minutes = int((i/60)%60)
#     hours = int(i/3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("things i wanna teach alfrid")
# alfrid =['femboy ethics', 'femboy behave' ,'how_to_femboy']
# print(alfrid)
# alfrid.append("femboy_milk")
# print(alfrid)

# for i in alfrid:
#     print(i)
    
# alfrid.remove("femboy_dih")
# print(alfrid)

#simple shoppin gcart program


# foods=[]
# prices = []
# total = 0 

# while True:
#     food = input("add your foods ")
#     if food == "q":
#         break
#     else:
#         foods.append(food)
#         price = int(input("enter the price $"))
#         prices.append(price)
# print("---------------your cart-----------------")
# for i in foods:
#     print(i)
# total = sum(prices)
# print(f"your total is {total}")

#num pad
num_pad = [["_","_","_"],["_","_","_"],["_","_","_"]]
player = "x"

while True:
    # Prints the board
    print("--------------------------------------------")
    for row in num_pad:
        for num in row:
            print(num, end=" ")
        print()
        
    # Asks the user input
    print("Please select the desired row and column to enter ")
    rows = int(input("Enter the row 1-3: ")) - 1
    col = int(input("Enter the col 1-3: ")) - 1
    
    # Check if the cell is already taken
    if num_pad[rows][col] != "_":
        print("That cell is already taken, pick another!")
        print()
        continue
        
    # Place the player's piece
    num_pad[rows][col] = player
    
    game_won = False
    
    # 1. Check Horizontal Win
    for row in num_pad:
        if row[0] == row[1] == row[2] == player:
            game_won = True
            
    # 2. Check Vertical Win
    for c in range(3):
        if num_pad[0][c] == num_pad[1][c] == num_pad[2][c] == player:
            game_won = True
            
    # 3. Check Diagonal Wins
    if num_pad[0][0] == num_pad[1][1] == num_pad[2][2] == player:
        game_won = True
    if num_pad[0][2] == num_pad[1][1] == num_pad[2][0] == player:
        game_won = True
    
    # End game if someone won
    if game_won:
        for row in num_pad:
            for num in row:
                print(num, end=" ")
            print()
        print(f"Player {player} wins!!!")
        break 
        
    # Swap players
    if player == "x":
        player = "0"
    else:
        player = "x"