import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe (by Queen 👑)")
window.geometry("300x350")
window.resizable(False, False)

# Variables
current_player = "X"
board = [" " for _ in range(9)]
buttons = []

# Function to check for a win
def check_win(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check for a draw
def check_draw():
    return " " not in board

# button click ka function
def button_click(index):
    global current_player

    if board[index] == " ":
        board[index] = current_player
        buttons[index]["text"] = current_player
        buttons[index]["state"] = "disabled"

        if check_win(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins! 🎉")
            window.quit()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a Draw! 🤝")
            window.quit()
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"

# Create 9 buttons
for i in range(9):
    button = tk.Button(window, text=" ", font=('Helvetica', 20), height=2, width=5,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the GUI event loop
window.mainloop()
