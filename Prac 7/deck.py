import  random

cardfaces= [i for i in range(2,11)]
cardfaces.extend(['Ace','Jack','King','Queen'])
suits=["Hearts","Diamonds","Clubs","Spades"]

deck=[]
for i in range(4):
    cards =[str(cardfaces[j])+" of "+suits[i]  for j in range(13)]
    for card in cards:
        deck.append(card)


print(deck)

random.shuffle(deck)
print("\n after shuffling the deck \n")
print(deck)


