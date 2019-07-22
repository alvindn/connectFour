#Alvin Nguyen 28864658
#Farnaz Safaei Takhtehfoulad 73932218
#
#Project 2
#

import connectfourshared
import connectfoursockets
import sys

def get_username() -> str:
    """Returns the username of the client's choice"""
    while True:
        username = input("Choose a Username: ").strip()
        if len(username) > 0:
            if " " in username:
                print("The username cannot have spaces! Please try again.")
            else:
                return username
        else:
            print("That username is empty. Please try again.")

def enter_protocol(username: str) -> str:
    """Returns a string with the protocol implemented and username of the client"""
    unique_protocol = "I32CFSP_HELLO"

    full_protocol_entry = unique_protocol + " " + username

    return full_protocol_entry

def check_initial_server_response(response: str, user_name: str) -> str:
    """Prints a string of the client's response from the server"""
    if response == "WELCOME " + user_name:
        print()
        print("WELCOME " + user_name + "!")
    elif response == "READY":
        pass
    else:
        print("Server does not recognize protocol. Closing connection...")
        print("Connection closed.")
        sys.exit()

def primary_user_input(connection: "connection") -> "GameState":
    """Returns a new GameState of the updated board given the
       server recognizes the correct protocol"""
    connectfourshared.welcome_message()
    new_board = connectfourshared.create_new_board()
    connectfourshared.print_board(new_board.board)
    print()
    user_name = get_username()
    full_protocol = enter_protocol(user_name)
    connectfoursockets.send_message(connection, full_protocol)
    protocol_response = connectfoursockets.receive_response(connection)
    check_initial_server_response(protocol_response, user_name)
    connectfoursockets.send_message(connection, "AI_GAME")
    ai_response = connectfoursockets.receive_response(connection)
    check_initial_server_response(ai_response, user_name)

    return new_board

def ask_user_move(current_board: "GameState") -> str:
    """Returns a string of the client's response to make a move"""
    connectfourshared.check_player_turn(current_board)
    player_response = connectfourshared.ask_drop_or_pop()
    column_entry = connectfourshared.check_valid_column_num(player_response)
    complete_response = player_response + " " + str(column_entry)
    return complete_response

def make_user_move(user_move: str, current_board: "GameState") -> "GameState":
    """Returns a GameState of the current board after the client's move"""
    user_move = user_move.split(" ")
    current_board = connectfourshared.update_board(current_board, user_move[0], int(user_move[1]))
    connectfourshared.print_board(current_board.board)
    return current_board
    
def send_move_to_ai(connection: "connection", user_move: str) -> None:
    """Sends the string message of the client to the server"""
    connectfoursockets.send_message(connection, user_move)

def receive_response_from_ai(connection: "connection") -> str:
    """Returns a string of the message response from the server"""
    server_response = connectfoursockets.receive_response(connection)
    return server_response

def check_server_response(connection: "connection", server_response: str) -> str:
    """Returns the validated string message of the server response according to the protocol"""
    if server_response == "OKAY":
        server_move = receive_response_from_ai(connection)
        return server_move
    else:
        return receive_response_from_ai(connection)

def translate_server_move(current_board: "GameState", server_move: str) -> "GameState":
    """Returns the GameState of the updated board after splitting the
       string version of the server's move"""
    server_move = server_move.split()
    update_board = connectfourshared.update_board(current_board, server_move[0], int(server_move[1]))
    return update_board

def player_vs_ai() -> None:
    """Executes the main function of the network version of client vs. server"""
    connection = connectfoursockets.user_connect()
    if connection == None:
        print("Server name and/or port # does not exist. Closing connection...")
        print("Connection closed.")
        sys.exit()
    current_board = primary_user_input(connection)
    while True:
        user_move = ask_user_move(current_board)
        current_board = make_user_move(user_move, current_board)
        send_move_to_ai(connection, user_move)
        server_response = receive_response_from_ai(connection)
        server_move = check_server_response(connection, server_response)
        if server_move == "READY":
            continue
        current_board = translate_server_move(current_board, server_move)
        receive_response_from_ai(connection)
        connectfourshared.print_board(current_board.board)
        if connectfourshared.check_winner(current_board) == True:
            break
        
if __name__ == "__main__":
    player_vs_ai()
