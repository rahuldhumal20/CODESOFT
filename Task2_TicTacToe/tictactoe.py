import tkinter as tk
from tkinter import messagebox
import math

# Create window
root = tk.Tk()
root.title("Tic Tac Toe - AI")

board = [" " for _ in range(9)]
buttons = []

# Check winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i

    if move is not None:
        board[move] = "O"
        buttons[move].config(text="O")

# Button click
def button_click(index):
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X")

        if check_winner("X"):
            messagebox.showinfo("Game Over", "You Win!")
            root.quit()
            return

        if is_draw():
            messagebox.showinfo("Game Over", "Draw!")
            root.quit()
            return

        ai_move()

        if check_winner("O"):
            messagebox.showinfo("Game Over", "AI Wins!")
            root.quit()
            return

        if is_draw():
            messagebox.showinfo("Game Over", "Draw!")
            root.quit()

# Create buttons
for i in range(9):
    button = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()
