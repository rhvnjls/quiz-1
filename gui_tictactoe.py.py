# GUI Tic-Tac-Toe Game using Tkinter

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.buttons = []

        for i in range(9):
            button = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def button_click(self, index):
        if self.buttons[index]["text"] == " ":
            self.buttons[index]["text"] = self.current_player

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif all(button["text"] != " " for button in self.buttons):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_positions = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for pos in win_positions:
            if (self.buttons[pos[0]]["text"] ==
                self.buttons[pos[1]]["text"] ==
                self.buttons[pos[2]]["text"] != " "):
                return True
        return False

    def reset_game(self):
        for button in self.buttons:
            button["text"] = " "
        self.current_player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

