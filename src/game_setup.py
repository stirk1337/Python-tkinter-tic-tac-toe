from tkinter import Tk, Label, Entry, Button


class GameSetup:
    """
    A class for setting up player names before starting the Tic-Tac-Toe game.

    This class provides a simple GUI for entering player names before starting the game.

    Attributes:
        root (Tk): The root window of the GUI.
        nicknames (tuple of str): A tuple containing the nicknames of the two players.

        Player1label (Label): Label displaying "Player 1" text.
        Player1Entry (Entry): Entry widget for entering Player 1's name.

        Player2label (Label): Label displaying "Player 2" text.
        Player2Entry (Entry): Entry widget for entering Player 2's name.

        Next (Button): Button to start the game.

    Methods:
        __init__(self): Initializes the player setup GUI.
        start_game(self, event): Retrieves player names and closes the setup window.

    """

    def __init__(self):
        """
        Initializes the player setup GUI.
        """
        self.root = Tk()
        self.root.geometry('270x70')
        self.root.title('Tic-Tac Toe')
        self.nicknames = ('', '')

        self.Player1label = Label(self.root, text='Player 1          ')
        self.Player1label.grid(row=0, column=0)

        self.Player1Entry = Entry(self.root)
        self.Player1Entry.grid(row=0, column=1)

        self.Player2label = Label(self.root, text='Player 2          ')
        self.Player2label.grid(row=1, column=0)

        self.Player2Entry = Entry(self.root)
        self.Player2Entry.grid(row=1, column=1)

        self.Next = Button(self.root, text='Start')
        self.Next.grid(row=2, column=1)
        self.Next.bind('<Button-1>', self.start_game)

        self.root.mainloop()

    def start_game(self, event):
        """
        Retrieves player names and closes the setup window.

        Args:
            event (tkinter.Event): The event object representing the button click.

        Returns:
            None
        """
        self.nicknames = (self.Player1Entry.get(), self.Player2Entry.get())
        self.root.destroy()
