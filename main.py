from tkinter import *
from tkinter import messagebox
from random import randint

def update(button):
	global turn
	global nicknames
	if button["text"] == " ":
		if turn % 2 == 0:
			button["text"] = "X"
		else:
			button["text"] = "O"
		turn += 1
		Turn_label["text"] = "Turn: " + nicknames[turn%2]
		root.update()

def if_winner(button1, button2, button3):
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        messagebox.showinfo("Winner", nicknames[0] +  " won!")
        exit()

    if button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        messagebox.showinfo("Winner", nicknames[1] + " won!")
        exit()

def check():
    if_winner(b1_1, b1_2, b1_3)
    if_winner(b2_1, b2_2, b2_3)
    if_winner(b3_1, b3_2, b3_3)
    if_winner(b1_1, b2_1, b3_1)
    if_winner(b1_2, b2_2, b3_2)
    if_winner(b1_3, b2_3, b3_3)
    if_winner(b1_1, b2_2, b3_3)
    if_winner(b1_3, b2_2, b3_1)
    if turn == 9:
        messagebox.showinfo("Draw!", "Draw!")
        exit()

turn = 0
nicknames = ["",""]

players = Tk()
players.geometry("270x70")
players.title("Tic-Tac Toe")

def next(event):
	global nicknames
	nicknames[0] = Player1Entry.get()
	nicknames[1] = Player2Entry.get()
	players.destroy()

Player1label = Label(players, text = "Player 1          ")
Player1label.grid(row = 0, column = 0)

Player1Entry = Entry(players)
Player1Entry.grid(row = 0, column = 1)

Player2label = Label(players, text = "Player 2          ")
Player2label.grid(row = 1, column = 0)

Player2Entry = Entry(players)
Player2Entry.grid(row = 1, column = 1)

Next = Button(players, text = "Start")
Next.grid(row = 2, column = 1)
Next.bind("<Button-1>", next)

players.mainloop()

root = Tk()
root.title("Tic-Tac Toe")
root.resizable(0,0)

def b1_1_event(event):
	update(b1_1)

def b1_3_event(event):
	update(b1_3)
          
def b1_2_event(event):
	update(b1_2)

def b2_1_event(event):
	update(b2_1)

def b2_2_event(event):
	update(b2_2)

def b2_3_event(event):
	update(b2_3)

def b3_1_event(event):
	update(b3_1)

def b3_2_event(event):
	update(b3_2)

def b3_3_event(event):
	update(b3_3) 

b1_1 = Button(root, text = " ")
b1_1.grid(row = 0, column = 0, ipadx = 40, ipady = 40)
b1_1.bind("<Button-1>", b1_1_event)

b1_2 = Button(root, text = " ")
b1_2.grid(row = 0, column = 1, ipadx = 40, ipady = 40)
b1_2.bind("<Button-1>", b1_2_event)

b1_3 = Button(root, text = " ")
b1_3.grid(row = 0, column = 2, ipadx = 40, ipady = 40)
b1_3.bind("<Button-1>", b1_3_event)

b2_1 = Button(root, text = " ")
b2_1.grid(row = 1, column = 0, ipadx = 40, ipady = 40)
b2_1.bind("<Button-1>", b2_1_event)

b2_2 = Button(root, text = " ")
b2_2.grid(row = 1, column = 1, ipadx = 40, ipady = 40)
b2_2.bind("<Button-1>", b2_2_event)

b2_3 = Button(root, text = " ")
b2_3.grid(row = 1, column = 2, ipadx = 40, ipady = 40)
b2_3.bind("<Button-1>", b2_3_event)

b3_1 = Button(root, text = " ")
b3_1.grid(row = 2, column = 0, ipadx = 40, ipady = 40)
b3_1.bind("<Button-1>", b3_1_event)

b3_2 = Button(root, text = " ")
b3_2.grid(row = 2, column = 1, ipadx = 40, ipady = 40)
b3_2.bind("<Button-1>", b3_2_event)

b3_3 = Button(root, text = " ")
b3_3.grid(row = 2, column = 2, ipadx = 40, ipady = 40)
b3_3.bind("<Button-1>", b3_3_event)

Turn_label = Label(root, text = "Turn: " + nicknames[0], font = 20)
Turn_label.grid(row = 1, column = 3)

while True:
    check()
    root.update()