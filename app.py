import tkinter as tk
import random

# Initialize the Tkinter app
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Global variables for game state
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
current_player = "X"
game_still_going = True
winner = None 
def play_game():
    while game_still_going:
        check_if_game_over()
    # Since the game is over, print the winner or tie
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

# Create a function for handling player moves
def handle_click(position):
    global current_player

    if board[position] == "-" and current_player == "X":
        board[position] = "X"
        buttons[position].config(text="X", state="disabled")
        current_player = "O"
        play_game()
        make_machine_move(current_player)

# Create a function for the machine's move (random)
def make_machine_move(current_player):
    if current_player == "O":
        empty_cells = [i for i, cell in enumerate(board) if cell == "-"]
        if empty_cells:
            machine_move = random.choice(empty_cells)
            board[machine_move] = "O"
            buttons[machine_move].config(text="O", state="disabled")
            current_player = "X"
            play_game()
def check_if_game_over():
    check_for_winner()
    check_for_tie()

# Create a function to check for a winner
def check_for_winner():
    # Implement your existing check_for_winner logic here
    global winner
    row_winner = check_rows()
    col_winner = check_columns()
    diagonal_winner = check_diagonal() 
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
def check_for_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False
def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    if row_3:
        return board[6]
    # or return None if there was no winner
    else:
        return None
def check_columns():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    if col_3:
        return board[2]
    # or return None if there was no winner
    else:
        return None
def check_diagonal():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    # or return None if there was no winner
    else:
        return None
# Create and configure buttons for the Tic-Tac-Toe grid
buttons = []
for i in range(9):
    row = i // 3
    col = i % 3
    button = tk.Button(root, text=" ", font=("normal", 20), width=6, height=2,
                       command=lambda i=i: handle_click(i))
    button.grid(row=row, column=col, sticky="nsew")
    buttons.append(button)

# Configure grid layout
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the game
root.mainloop()
