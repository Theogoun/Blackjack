from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import pandas as pd
import time

# Deck related setup
Deck = pd.read_json("Python/Free Time Projects/Blackjack/Deck.json")    # The deck with values and faces
Order = np.arange(52)            # The order of the cards
o = 0                            # Counter for the cards taken from the deck assuring we wont get the same card twice
np.random.shuffle(Order)         # The shuffled order of the cards

# Getting a card from the Deck in the order of the "Order" 
def GetCard(Hand):
    global o,Order,Deck
    Current_Value = Hand.get()

    Last_Card = Deck["Value"][Order[o]]                     # The card that will be added
    if Last_Card == "Ace" and (Current_Value + 11 > 21):
        Last_Card = 1
    elif Last_Card == "Ace":
        Last_Card = 11
    elif isinstance(Last_Card,int):
        Last_Card = Deck["Value"][Order[o]]
    else:
        Last_Card = 10
    o += 1

    New_Value = Current_Value + Last_Card
    Hand.set(New_Value)

# Mainframe setup--------------------------------------------------------------GUI
root = Tk()
root.title("Blackjack")
mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Player's hand----------------------------------------------------------------CARDS
Hand = IntVar()
Hand.set(0)

GetCard(Hand)
GetCard(Hand)

# Dealer's Hand
Dealer = IntVar() # Dealer's hand (Value)
Dealer.set(0)
Up_Card = GetCard(Dealer)                  # Gets a card like the player

if Deck["Value"][Order[o]] == int:         # Gets a hidden card
    Hole_Card = Deck["Value"][Order[o]]
elif Deck["Value"][Order[o]] == "Ace":
    Hole_Card = 11
else:
    Hole_Card = 10
o += 1



# Defining Buttons-------------------------------------------------------------GUI
def Button_Hit():
    GetCard(Hand)
    if Hand.get() > 21:
        messagebox.showinfo(message='BUST, you lost')
        root.destroy()

def Button_Stand():
    Dealer.set(Dealer.get() + Hole_Card)
    root.update_idletasks()
    time.sleep(1)

    if Dealer.get() < 17 and Dealer.get() <= Hand.get():
        GetCard(Dealer)
        root.update_idletasks()
        time.sleep(1)

    if Dealer.get() > 21:
        messagebox.showinfo(message='You won, Dealer busted')
        root.destroy()
        return
    
    # Checking Hands and determining winner
    if Hand.get() < Dealer.get():
        messagebox.showinfo(message='You lost, loser >:)')
    elif Hand.get() > Dealer.get():
        messagebox.showinfo(message='You won, Congrats!')
    else:
        messagebox.showinfo(message='Push, its a tie')
    root.destroy()

# Variable labels
ttk.Label(mainframe, textvariable=Hand).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, textvariable=Dealer).grid(column=2, row=1, sticky=(W, E))

# Static labels
ttk.Label(mainframe, text="Your Hand").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="The Dealer").grid(column=1, row=1, sticky=W)

# Buttons
Hit = ttk.Button(mainframe, text='Hit', command=Button_Hit)
Hit.grid(column=1, row=3, sticky=W)
Stand = ttk.Button(mainframe, text='Stand', command=Button_Stand)
Stand.grid(column=2, row=3, sticky=W)






for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()