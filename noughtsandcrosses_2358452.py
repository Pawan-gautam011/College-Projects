"""
This is a nought and cross game where Player1 plays against the computer
"""
import json
import random
random.seed()


def draw_board(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0][0], board[0][1], board[0][2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[1][0], board[1][1], board[1][2]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(board[2][0], board[2][1], board[2][2]))
    print("\t     |     |")
    print("\n")


def welcome(board):
    """
    This function prints the welcome message for Player1 and draws the board layout in terminal
    by calling the draw board function
      """
    # prints the welcome message
    print("Welcome to the \"Unbeatable Noughts and Crosses\" game. \nThe board layout is shown below:")

    # display the board by calling draw_board(board)
    draw_board(board)

    # print the message
    print("When prompted, enter the number corresponding to the square you want.")


def initialise_board(board):
    """
    This function initialize the board by setting all the cells to empty so that Player1
    and computer can enter the 'X' and 'O' respectively
    """
    # update elements of the board list to ' '
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '

    # call the board function and pass the argument
    draw_board(board)
    return board


def get_player_move(board):

    # prompt the Player1 for input
    Player1 = None  
    while Player1 is None:
        try:
            # prompt Player1 where they want to put the X
            print("\n")
            Player1 = int(input("Choose your square:\n 1 2 3 \n 4 5 6 \n 7 8 9 : "))
            # check if Player1 has entered valid cell or not
            if not ((Player1 > 0) and (Player1 < 10)):
                print("number should be between 1 to 9")
                Player1 = None
            else:
                #convert the Player1 input into row and column to fill the Player1 entered cell
                row = (Player1 - 1) // 3
                col = (Player1 - 1) % 3

                # check if cell is already filled or not
                if board[row][col] != " ":
                    print("place is already filled!!!")
                    Player1 = None
                else:  
                    # if Player1 input is valid return row and column
                    return row, col

        # print error message in case of invalid input
        except ValueError:
            print("Invalid Input")
        except Exception as error:
            print(f"Error:{error}")


def choose_computer_move(board):
    """
    This function picks a move for computer and also validates it by checking
    if the cell is empty or not
    """
    computer = None
    while computer is None:
        try:
            # generate random number from 1-9
            computer = random.randint(1, 9)

            # convert the number into row and colum to fill in "O"
            row = (computer - 1) // 3
            col = (computer - 1) % 3
            if board[row][col] != " ":
                computer = None
            else:
                return row, col
        except Exception as error:
            print(f"Error:{error}")


def check_for_win(board, mark):
    """
    This function checks all possible winning conditions
    """
    # develop code to check if either the player or the computer has won
    try:
        # check row
        for row in range(3):
            if board[row][0] == mark and board[row][1] == mark and board[row][2] == mark:
                return True

        # check columns
        for col in range(3):
            if board[0][col] == mark and board[1][col] == mark and board[2][col] == mark:
                return True

        # check diagonals
        if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
            return True
        if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
            return True
    except Exception as error:
        print(f"Error: {error}")

    # if no one wins return false
    return False


def check_for_draw(board):
    """
    This function checks for the draw conditions
    """
    # develop cope to check if all cells are occupied
    try:
        # check if any cell is empty or not
        for row in board:
            for cell in row:
                if cell == " ":
                    return False
        return True
    except Exception as error:
        print(f"Error:{error}")


def play_game(board):
    """ 
    This is the main that connects all the previous build function so that the game can be played
    """
    try:
        initialise_board(board)
         # initialize terminate as false
        terminate = False 
        outcome = None  
        while not terminate:
            # Player's move
            player_mark = 'X'
            print("\n")
            print(f"Player's turn (mark: {player_mark})")
            print("")
            row, col = get_player_move(board)
            board[row][col] = player_mark
            draw_board(board)

            # Check if player has won
            win = check_for_win(board, player_mark)
            if win:
                print("\n")
                print("Player wins!")
                print("")
                outcome = 1
                terminate = True

            # Check for a draw
            if check_for_draw(board):
                print("\n")
                print("Draw!")
                print("")
                outcome = 0
                terminate = True

            if not terminate:
                # Computer's move
                computer_mark = 'O'
                print("\n")
                print(f"Computer's turn (mark: {computer_mark})")
                print("")
                row, col = choose_computer_move(board)
                board[row][col] = computer_mark
                draw_board(board)

                # Check if computer has won
                if check_for_win(board, computer_mark):
                    print("\n")
                    print("Computer wins!")
                    print("")
                    outcome = -1
                    terminate = True
    except Exception as error:
        print(f"Error:{error}")

    return outcome 


def menu():
    """
    This functions displays the menu and asks the Player1 what they want to do
    """

    option = ["1", "2", "3", "q"]
    terminate = False  
    while not terminate:
        try:
            print("\n-")
            choice = input("""Enter one of the following option:
            1- Play the game
            2- Save your score in the leaderboard
            3- Load and display the leaderboard
            q- End the program
            1,2,3 or q?  """)
            # check if Player1 has entered the valid option or not
            if choice not in option:
                print("Invalid option")
            else:
                terminate = not terminate
        except Exception as error:
            print(f"Error: {error}")

    return choice


def load_scores():
    """
    This functions loads the score saved in the leaderboard.txt text file
    """
    leaders = {}
    try:
        with open("leaderboard.txt", "r") as file:
            data = json.load(file)
            for item in data:
                name = item.get("name", "")
                score_str = item.get("score", "")
                try:
                    score = int(score_str)
                    leaders[name] = score
                except ValueError:
                    print(f"Invalid score for {name}: {score_str}")
    except (PermissionError, FileNotFoundError, EOFError, Exception) as error:
        print(f"Error: {error}")
    return leaders


def save_score(score):
    """
    if Player1 chose to save the score this function will prompt the Player1 for name
    and save their score in the leaderboard.txt text file
    """
    #ask Player1 for input name
    print("||")
    name = input("Enter your name: ")
    print("||")
    
    #add empty list to add player name and score
    data = []

    #open leaderboard
    try:
        with open("leaderboard.txt", "r") as file:
            data = json.load(file)
    except (PermissionError, EOFError, ValueError) as error:
        print(f"Error: {error}")

    # if there is no file create a leaderboard list
    except FileNotFoundError:
        data = []

    # add new score to a leaderboard
    data.append({
        "name": name,
        "score": score
    })

    # save player name and score in file
    with open("leaderboard.txt", "w") as file:
        json.dump(data, file)
    print("")
    print("Name and score saved!!")
    print("")


def display_leaderboard(leaders):
    """
    This function will load the player name and their score and display it
    """
    # print leaderboard
    print("")
    print(" Leader Board")
    print("")
    # iterate through each item in dictionary and print them
    try:
        for key, value in leaders.items():
            print("\t", key, value)

    # catch and print the error in case of any
    except Exception as error:
        print(f"Error: {error}")
