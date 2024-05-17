import pandas as pd
import json

Deck = []
O = 0                       #Order
#adding the aces and faces
for i in range(4):          #value
    match i:
        case 0:
            x = "Ace"
        case 1:
            x = "Jester"
        case 2:
            x = "Queen"
        case 3:
            x = "King"
    for j in range(4):      #suits
        match j:
            case 0:
                card = [O, x,"of Hearts"]
                O += 1
            case 1:
                card = [O, x,"of Diamonds"]
                O += 1
            case 2:
                card = [O, x,"of Clubs"]
                O += 1
            case 3:
                card = [O, x,"of Spades"]
                O += 1
        Deck.append(card)

#adding the numbers
for i in range(2,11):       #values
    for j in range(4):      #suits
        match j:
            case 0:
                card = [O, i,"of Hearts"]
                O += 1
            case 1:
                card = [O, i,"of Diamonds"]
                O += 1
            case 2:
                card = [O, i,"of Clubs"]
                O += 1
            case 3:
                card = [O, i,"of Spades"]
                O += 1

        Deck.append(card)

df = pd.DataFrame(Deck, columns=["Order","Value","Suit"])
df.to_json("Deck.json")
