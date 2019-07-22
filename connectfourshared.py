#Alvin Nguyen 28864658
#Farnaz Safaei Takhtehfoulad 73932218
#
#Project 2
#

import connectfour

def welcome_message() -> str:
    """Prints a string welcome message for the client"""
    print("Welcome to Connect Four!")
    print()

def red_or_yellow(number: int) -> str:
    """Returns a string of the name of which player's turn it currently is"""
    if number == 1:
        return "RED"
    else:
        return "YELLOW"
    
def print_board(board: [[int]]) -> str:
    """Prints out the board using the current GameState's board"""
    print()
    for col_num in range(1, connectfour.BOARD_COLUMNS + 1):
        print(str(col_num) + " ", end = " ")
    print()
    for row in range(connectfour.BOARD_ROWS):
        row_str = ''
        for col in range(connectfour.BOARD_COLUMNS):
            row_str += str(board[col][row])
        spaced_board = space_items(row_str)
        replace_player = format_board_zero(spaced_board)
        format_board_player(replace_player)
    print()

def format_board_zero(board: str) -> str:
    """Returns a new string of replaced 0's with '.' for the board"""
    new_str = ""
    new_str = board.replace("0", ".")
    return new_str

def format_board_player(board:str) -> str:
    """Prints a new string replacing the original 1's and 2's with 'R' and 'Y' respectively"""
    new_str = ""
    new_str = board.replace("1", "R")
    new_str = new_str.replace("2", "Y")
    print(new_str)

def space_items(board: str) -> str:
    """Returns a newly spaced string of the board"""
    new_board = ""
    for char in board:
        new_board += char + "  "
    return new_board

def create_new_board() -> "GameState":
    """Returns a GameState for a new game"""
    new_board = connectfour.new_game()
    return new_board

def update_board(current_gamestate: "GameState", drop_or_pop: str, col_num: int) -> "GameState":
    """Returns an updated GameState of the game depending on the user's choice
       of 'DROP' or 'POP'"""
    while True:
        if drop_or_pop == "DROP":
            try:
                updated_board = connectfour.drop(current_gamestate, col_num - 1)
                return updated_board
                break
            except connectfour.InvalidMoveError:
                print("Sorry that column is full! Try again.")
                return current_gamestate
        elif drop_or_pop == "POP":
            try:
                updated_board = connectfour.pop(current_gamestate, col_num - 1)
                return updated_board
                break
            except connectfour.InvalidMoveError:
                print("Sorry that is not your piece! Try again.")
                return current_gamestate
        else:
            print("Sorry that's an invalid response. Try again.")

def check_valid_column_num(player_response: str) -> int:
    """Returns the number of column choice of client as int"""
    while True:
        try:
            col_num = int(input("Choose a column # to " + player_response + " your piece in: "))
            if 1 <= col_num <= connectfour.BOARD_COLUMNS:
                return col_num
                break
            else:
                print("Sorry that is an invalid column number. Try again.")
        except ValueError:
            print("Enter an integer (1-" + str(connectfour.BOARD_COLUMNS) + "): ")
            pass
        
def check_player_turn(current_gamestate: "GameState") -> str:
    """Prints the current player's color turn"""
    player_color = red_or_yellow(current_gamestate.turn)
    print("\nIt's your turn " + str(player_color) + " player.")
    
def ask_drop_or_pop() -> str:
    """Returns the string version of the choice of the client"""
    while True:
        player_answer = input("Do you want to 'DROP' or 'POP'? ")
        if player_answer == "DROP":
            return player_answer
            break
        elif player_answer == "POP":
            return player_answer
            break
        else:
            print("Sorry that is an invalid response. Try again.")
            
def check_winner(current_gamestate) -> bool:
    """Returns True or False depending on if a winner is decided"""
    if connectfour.winner(current_gamestate) == 1:
        print("\nRED PLAYER IS THE WINNER!")
        return True
    elif connectfour.winner(current_gamestate) == 2:
        print("\nYELLOW PLAYER IS THE WINNER!")
        return True
    else:
        None
    
