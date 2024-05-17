import pandas as pd
import json

Deck = []

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
                card = [x,"of Hearts"]
            case 1:
                card = [x,"of Diamonds"]
            case 2:
                card = [x,"of Clubs"]
            case 3:
                card = [x,"of Spades"]
        Deck.append(card)

#adding the numbers
for i in range(2,11):       #values
    for j in range(4):      #suits
        match j:
            case 0:
                card = [i,"of Hearts"]
            case 1:
                card = [i,"of Diamonds"]
            case 2:
                card = [i,"of Clubs"]
            case 3:
                card = [i,"of Spades"]

        Deck.append(card)

df = pd.DataFrame(Deck, columns=["Value","Suit"])
df.to_json("Deck.json")