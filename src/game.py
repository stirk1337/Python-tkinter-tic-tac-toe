import tkinter
from tkinter import Tk, Button, messagebox, Label


class Game:
    """
    A simple Tic-Tac-Toe game using Tkinter GUI.

    This class creates a graphical user interface for a two-player Tic-Tac-Toe game.
    Players take turns clicking on the grid cells to place their symbols ('X' or 'O').
    The game checks for a winning combination or a draw and displays the result.

    Attributes:
        nicknames (tuple of str): A tuple containing the nicknames of the two players.
        turn (int): The current turn number in the game.
        winning_combinations (list of list of tuple): List of winning combinations.
            Each combination is a list of coordinate tuples representing the cells.
        buttons (list of Button): List of buttons in the game grid.
        board (list of list of Button): 2D list representing the game grid.
        turn_label (Label): Label indicating whose turn it is.
        root (Tk): The root window of the game.

    Methods:
        __init__(self, nicknames): Initializes the game by creating the GUI elements.
        update(self, event, button): Handles the button click event and updates the game state.
        check_for_winner(self): Checks for a winning combination in the current game state.
    """

    def __init__(self, nicknames: str):
        """
        Initializes the game by creating the GUI elements.

        Args:
            nicknames (list of str): A list containing the nicknames of the two players.
        """
        self.root = Tk()
        self.root.title('Tic-Tac Toe')
        self.root.resizable(False, False)

        self.nicknames = nicknames
        self.turn = 0
        self.winning_combinations = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        self.buttons = []
        self.board = []

        for i in range(3):
            self.board.append([])
            for j in range(3):
                button = Button(self.root)
                button.grid(row=i, column=j, ipadx=40, ipady=40)
                button.bind('<Button-1>', lambda event, btn=button: self.update(event, btn))
                self.buttons.append(button)
                self.board[i].append(button)

        self.turn_label = Label(self.root, text='Turn: ' + self.nicknames[0], font=20)
        self.turn_label.grid(row=1, column=3)

        self.root.mainloop()

    def update(self, event, button: Button):
        """
        Handles the button click event and updates the game state.

        Args:
            event (tkinter.Event): The event object representing the button click.
            button (Button): The button widget that was clicked.

        Returns:
            None
        """
        if not button['text']:
            button['text'] = 'O' if self.turn % 2 else 'X'
            self.turn += 1
            self.turn_label['text'] = 'Turn: ' + self.nicknames[self.turn % 2]

            def end_game(title: str, message: str):
                messagebox.showinfo(title, message)
                exit()

            winner = self.check_for_winner()
            if winner is not None:
                end_game('Winner', self.nicknames[winner] + ' won!')

            if self.turn == 9:
                end_game('Draw', 'Draw!')

            self.root.update()

    def check_for_winner(self) -> int | None:
        """
       Checks for a winning combination in the current game state.

       Returns:
           int or None: Index of the winning player ('X' or 'O'), or None if no winner.
        """
        for index, player_symbol in enumerate(['X', 'O']):
            for combination in self.winning_combinations:
                if all(self.buttons[row * 3 + col]['text'] == player_symbol for row, col in combination):
                    return index
        return None
