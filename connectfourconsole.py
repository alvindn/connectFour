#Alvin Nguyen 28864658
#Farnaz Safaei Takhtehfoulad 73932218
#
#Project 2
#

import connectfourshared
       
def player_vs_player() -> None:
    """Executes the player vs. player console version of Connect Four using
       imported modules from connectfourshared.py
    """
    new_board = connectfourshared.create_new_board()
    current_board = new_board
    connectfourshared.welcome_message()
    connectfourshared.print_board(new_board.board)
    while True:
        connectfourshared.check_player_turn(current_board)
        player_response = connectfourshared.ask_drop_or_pop()
        column_entry = connectfourshared.check_valid_column_num(player_response)
        current_board = connectfourshared.update_board(current_board, player_response, column_entry)
        connectfourshared.print_board(current_board.board)
        if connectfourshared.check_winner(current_board) == True:
            break
    
if __name__ == '__main__':
    player_vs_player()
    

