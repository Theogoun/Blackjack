# Blackjack

A small project that simulates a single hand of blackjack with standard rules in python using tkinter.
I started this small project to practice data analysis with json files while also trying out UI through code.

## A Brief Explanation

A lot of comments exist in the code but this is a brief showcase of what is what:

- The "Making a deck" program makes a json file with all the cards in a deck in an orderly fashion, this deck is not in the normal order of a new deck it is in the order that was easiest and most efficient way i could write in code. The result is the "Deck" json file that has each card's value and suit.

- "Blackjack.py" is where everything happens, first it shuffles the deck by creating a new list that has the order of the cards that will be selected, that way we dont need to clone or edit the original deck as we will consult the "Order" list on which card's turn it is to be selected. After that a function is defined for us to select each card that checks the card's value while also making adjustments for the Aces. After the interface pops up the house and the player get a card and the house gets a hidden card, the player is then prompted by 2 buttons to either hit or stay, the standard rules apply and the game checks who wins after the player stays or busts and announces it with a pop up before the game closes.

## Future of this project

As there is a funtion to get cards and a way to generate a whole deck it would be easy to go for more card games using parts of this project, it could also benefit from some visuals. There is also the very easy change/addition of a mode without a deck, or an "unlimited" deck, as most blackjack tables use multiple decks and don't rely as much on the finite number of cards and are more random.
