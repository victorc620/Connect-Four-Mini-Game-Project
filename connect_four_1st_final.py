#Construct the board with row and colume defined by user input----------------------
def board_construct(row, colume):
    board_temp = []

    colum_indicator = ""
    for i in range(1,colume+1):
        i = str(i)
        colum_indicator +="  "+i+" "
    board_temp.append(colum_indicator)

    square_horizontal = "+---" * (colume) + "+"
    square_straight = ("|   ") * colume + "|"

    for height in range(row):
        board_temp.append(square_horizontal)
        board_temp.append(square_straight)
        height +=1

    board_temp.append(square_horizontal)
    for i in board_temp:
        print(i)
    return board_temp


#Player place token and update list---------------------------------
def place_token(token):
    for i in range(2, (row+1)*2, 2):
        if board[-i][(place_colume-1)*4+2] == "o" or board[-i][(place_colume-1)*4+2] == "x": #if coin exist, move up one row
            continue
        else:
            if 0<place_colume <=colume:
                board[-i] = board[-i][:(place_colume-1)*4+2]+token+board[-i][(place_colume-1)*4+3:]
                for a in board:
                    print(a)
                return board[-i]
            else:
                print("Error, colume dosen't exist!")
            break

#Check for winner after each token placment-----------------------------
def check_winner(token):
    connect_count = 0

#i. Check for horizontal connection
    for check_row in range(2, (row+1)*2, 2): #Iterate from the bottom row_number
        for check_colume in range(2,(colume-1)*4+3, 4): #Iterate from the left colume_number (i,e check right cell for horizontal conntection)
            if board[-check_row][check_colume] == token: #Check for horizontal connect four
                connect_count+=1
                if connect_count == win_condition:
                    return True
            else:
                connect_count = 0

#ii. Check for vertical connection
    for check_colume in range(2,(colume-1)*4+3, 4): #Iterate from the left colume_number
        for check_row in range(2, (row+1)*2, 2): #Iterate from the bottom row_number (i.e. Check upward cell for vertical connection)
            if board[-check_row][check_colume] == token: 
                connect_count+=1
                if connect_count == win_condition:
                    return True
            else:
                connect_count = 0

#iii. Check for diagonal connection
    for current_colume in range(2,(colume-1)*4+3, 4): #Check current cell from the left colume 
        for current_row in range(2, (row+1)*2, 2): #Check current row forom the bottom row
            next_colume_rlist = list(range(current_colume,(colume-1)*4+3, 4))
            next_colume_llist = list(range(current_colume, 0, -4))
            next_row_list = list(range(current_row, (row+1)*2, 2))
            
            #Check upper right direction 
            try:
                if board[-current_row][current_colume] == token: #if current colume have token, check next cell  
                    for next_colume, next_row in zip(next_colume_rlist, next_row_list): #The first next_xx is the same as current cell, then iterate to next cell
                        if board[-next_row][next_colume] == token:
                            connect_count+=1
                            if connect_count == win_condition:
                                return True
                        else:
                            connect_count = 0
                            break
            except:
                pass
            
            #Check upper left connection
            try:
                if board[-current_row][current_colume] == token:
                    for next_colume, next_row in zip(next_colume_llist, next_row_list): #The first next_xx is the same as current cell, then iterate to next cell
                        if board[-next_row][next_colume] == token:
                            connect_count+=1
                            if connect_count == win_condition:
                                return True
                        else:
                            connect_count = 0
                            break
            except:
                pass
                



###__________Main Function__________###

game = True

while game == True: #Provide function for users to play again
    
#-----1. Ask users to decide board size-----

    row = int(input("How many row is the board? "))
    colume = int(input("How many colume is the board? "))
    win_condition = int(input("How many continuous connection is needed for the win? "))
    board = board_construct(row, colume)

#-----2. Player begin to place token-----

#Loop until someone win
#How to win: Connect 4 of the same colored discs in a row (either vertically, horizontally, or diagonally)

    while True:

        #Player x
        place_colume = int(input("Trying to place an x in colume:"))
        place_token("x")
        winner_x = check_winner("x")
        if winner_x == True:
            print("x is the winner!")
            break


        # #Player o
        place_colume = int(input("Trying to place an o in colume:"))
        place_token("o")
        winner_o = check_winner("o")
        if winner_o == True:
            print("o is the winner!")
            break
        
    #Restart after game?
    replay = str(input("Do you want to play again (Y/N)? "))
    
    while replay != "Y" and replay != "N":
        replay = str(input("Your input is invalid, Please enter Y or N: "))
    
    if replay == "Y":
        game = True
    elif replay == "N":
        print("Thanks for playing, see you next time!")
        exit()