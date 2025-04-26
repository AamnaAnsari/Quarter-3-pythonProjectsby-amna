import tkinter as tk
from tkinter import messagebox

# Sudoku Solver Logic (Backtracking)
def solve(board):
    find = find_empty(board)
    if not find:
        return True  # Solved
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0  # Undo

    return False

def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # (row, col)
    return None

# Tkinter GUI Class
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver - Backtracking + Tkinter GUI")
        self.cells = {}
        self.board = [
            [0 for _ in range(9)] for _ in range(9)
        ]
        self.make_grid()
        self.make_buttons()

    def make_grid(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            for j in range(9):
                cell = tk.Entry(frame, width=2, font=('Arial', 24), justify='center', bd=2, relief='ridge')
                cell.grid(row=i, column=j, padx=3, pady=3)
                self.cells[(i, j)] = cell

    def make_buttons(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        solve_btn = tk.Button(btn_frame, text="Solve", command=self.solve_board, width=10, bg='lightblue')
        solve_btn.grid(row=0, column=0, padx=10)

        clear_btn = tk.Button(btn_frame, text="Clear", command=self.clear_board, width=10, bg='lightcoral')
        clear_btn.grid(row=0, column=1, padx=10)

    def get_board(self):
        for i in range(9):
            for j in range(9):
                val = self.cells[(i, j)].get()
                if val == '':
                    self.board[i][j] = 0
                else:
                    try:
                        num = int(val)
                        if 1 <= num <= 9:
                            self.board[i][j] = num
                        else:
                            raise ValueError
                    except:
                        messagebox.showerror("Invalid Input", "Only numbers 1-9 allowed!")
                        return False
        return True

    def solve_board(self):
        if not self.get_board():
            return
        if solve(self.board):
            for i in range(9):
                for j in range(9):
                    self.cells[(i, j)].delete(0, tk.END)
                    self.cells[(i, j)].insert(0, str(self.board[i][j]))
        else:
            messagebox.showinfo("No Solution", "This Sudoku cannot be solved.")

    def clear_board(self):
        for i in range(9):
            for j in range(9):
                self.cells[(i, j)].delete(0, tk.END)
        self.board = [[0 for _ in range(9)] for _ in range(9)]

# Main Execution
if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
