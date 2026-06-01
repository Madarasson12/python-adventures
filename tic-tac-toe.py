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