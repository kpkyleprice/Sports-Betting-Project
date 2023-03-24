# Store Parlay bets
Gamble = {}
# add leg to ticket
def add_leg():
    if ML != 0:
        Gamble.append(Gamble)
# first part of equation
def fave():
    ML/bet + 1

def dog():
    bet/ML + 1


# calculate potential winnings
def calculate():
    if Underdog:
        dog()
    elif Favorite:
        fave()

# input spreads
ML = int(input('What is the ML for your Bet? '))
while ML != 0:
    add_leg()
    if ML == "quit":
        break
    else:
        print("Invalid")
# Underdogs are +101 and above Favorites are -101 or higher 
Underdog = ML > 100 
Favorite = ML < -100

#wager
bet = int(input('How much are you betting '))
if bet == 0:
    print("You need to bet something")
elif bet < 0:
    print("Invalid")

# takes decimal from bet and spread and multiplies it by wager
Gamble[fave() + dog()] * bet

print(Gamble)
