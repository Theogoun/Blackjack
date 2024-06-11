import numpy as np
import pandas as pd
import json

D = pd.read_json("Deck.json")    #The deck
O = np.arange(52)                #The order
o = 0                            #Current order
np.random.shuffle(O)             #The Shuffle

lost = 0                         #Indicator you lost
#indicator of Hit or stay is Flag

#Hand of The House and the player
MHand = 0
Hand = 0

#The House's Hand
Flag = 1

#Getting a card from the shuffled deck LC standing for Last Card added
def GetCard(Hand):
    global o,O,D
    LC = D["Value"][O[o]]
    if LC == "Ace" and (Hand+11 > 21):
        LC = 1
    elif LC == "Ace":
        LC = 11
    elif isinstance(LC,int):
        LC = D["Value"][O[o]]
    else:
        LC = 10
    o += 1
    return LC


MHand += GetCard(MHand)
MHand1 = MHand                   #The House's visible card
MHandc = 0                       #The House's number of hidden cards
while Flag==1:
    LC = GetCard(MHand)
    MHand += LC
    MHandc += 1
    if MHand >=21:
        MHand -= LC
        MHandc -= 1
        o -= 1
        Flag = 0
        print(f"The House has: {MHand1} with {MHandc} hidden cards")

#The House has Blackjack
if MHand == 21 and MHandc==2:
    lost == 1
    print("The house got Blackjack :)")

#Your Hand
Flag = 1
while Flag==1 and lost ==0:
    if Hand <= 21:
        print(f"you have: {Hand}")
        Flag = input("type 1 to hit and 0 to stay:")
        Flag = int(Flag)
    else:
        print("You Busted")
        lost = 1
        break
    if Flag ==1:
        LC = GetCard(Hand)
        Hand += LC

if Hand > MHand and lost == 0:
    print(f"you won, you had {Hand}, The House had {MHand}")
else:
    print(f"you lost, you had {Hand}, The House had {MHand}")