import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

#global playing
playing = True

# Main Classes
class Card:

    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
        #self.value = values[rank] #have this in hand class

    def __str__(self):
        return(self.rank + " of " + self.suit)
class Deck:

    def __init__(self):

        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):

        deck_comp = ''
        for card in self.deck:

            deck_comp += '\n '+card.__str__() # add each card object's print string
        return 'The deck has: ' + deck_comp
            #print(card) I THINK You dont want to print..

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
        #return self.deck.pop() #this doesnt return the val
class Hand:

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):

        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
class Chips:

    def __init__(self,total=1000):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 10

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self. bet

# ------Functions------
def take_bet(chips):
    #Asks for user input for bet, bets are kept track by Chips Class
    while True:
        try:
            chips.bet = int(input('Enter a bet between 0 and 500!'))
            if 0 < chips.bet < 500:
                print('\n')
                break
            else:
                print('Bet out of bounds. Try again')
        except:
            print('Bet not a number. Please choose a bet between 0 and 500')

def hit(deck,hand):

    #Adds a Card to Hand, uses functions of card class to add
    hand.add_card(deck.deal())
    hand.adjust_for_ace() #This checks if greater than 21, if so subtract 10

def hit_or_stand(deck,hand):

    #Asks user if they want to hit or stand.
    global playing
    playing = True
     # to control an upcoming while loop
    while True:

        userchoice_ = input("\nHit or Stand?").lower()
        print(userchoice_)
        if userchoice_ == "hit":
            print('\nwe hit\n')
            hit(deck,hand)
            break
        elif userchoice_ == "stand":
            print('\nwe stand\n')
            playing = False
            break
        else:
            print("Invalid input...")
def show_some(player,dealer):

    #Shows all of the players cards, but hides one of the dealers.
    print('Your hand:')
    for card_ in player.cards: print(card_)
    print(f'Your total: {player.value}')

    print('\nDealer hand:')
    for count_,card_ in enumerate(dealer.cards):

        if count_ == 0:
            print('XXXXXXX')
        else:
            print(card_)
    #print(dealer.value) #I think this is hidden til end.
def show_all(player,dealer):
    #Shows all of player and dealer cards.
    for card_ in player.cards: print(card_)
    print(f'Your total: {player.value}\n')

    for card_ in dealer.cards: print(card_)
    print(f'Dealer total: {dealer.value}')
def player_busts(player,dealer):
    #Called when player busts. Shows all cards, subtracts bet
    global playing
    show_all(player,dealer)
    chips.lose_bet()
    print(f'\nYou busted. {chips.bet} in chips have been removed from your pot.')
    playing = False #Global var..
def player_wins(player,dealer):
    #called when player wins.  Shows all cards, adds bet
    global playing
    show_all(player,dealer)
    chips.win_bet()
    print(f'\nYou Win! {chips.bet} in chips have been added to your pot.')
    playing = False #Global var..
def dealer_busts(player,dealer):

    #Same as player bust.
    show_all(player,dealer)
    chips.win_bet()
    print(f'\nDealer busted, and you win! {chips.bet} in chips have been added to your pot.')

def dealer_wins(player,dealer):

    #Same as player_wins, but opposite chips command
    show_all(player,dealer)
    chips.lose_bet()
    print(f'Dealer wins. {chips.bet} in chips have been removed from your pot.')

def push():

    #called when dealer draws 22.
    print('Game ends in a draw.')

# Main program
chips = Chips() #Setting up variable to keep track of bets

while True: #The game Starts
    print('\nWelcome to Blackjack!')

    game_deck = Deck()
    game_deck.shuffle()

    # Setup of Player hand
    player_hand = Hand()
    player_hand.add_card(game_deck.deal())
    player_hand.add_card(game_deck.deal())

    # Setup of Dealer hand
    dealer_hand = Hand()
    dealer_hand.add_card(game_deck.deal())
    dealer_hand.add_card(game_deck.deal())

    # Setup of Chips
    take_bet(chips) #my 1st prompt
    show_some(player_hand,dealer_hand)

    playing = True
    gameover = False

    while playing:

        #Looping for player, playing their hand
        if player_hand.value == 21:
            player_wins(player_hand,dealer_hand)
            gameover = True

        elif player_hand.value > 21:
            player_busts(player_hand,dealer_hand)
            gameover = True

        else:
            hit_or_stand(game_deck,player_hand)
            show_some(player_hand,dealer_hand)

    if gameover == False: #Checks if player won/busted, before running
                          #Dealer Code

        while True: #Dealer now plays hand.

            if (dealer_hand.value > player_hand.value) \
                & (dealer_hand.value < 21):
                dealer_wins(player_hand,dealer_hand)
                gameover = True
                break

            if dealer_hand.value == 21:
                dealer_wins(player_hand,dealer_hand)
                gameover = True
                break

            elif dealer_hand.value == 22:
                push()
                gameover = True
                break

            elif dealer_hand.value == 17: #player stands and dealer == 17
                break

            elif dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand)
                gameover = True
                break

            dealer_hand.add_card(game_deck.deal())

    if gameover == False: #Checks if player won/busted, before running
                          #Dealer Code

        if player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand)
        else:
            dealer_wins(player_hand,dealer_hand)

    print(chips.total)

    REPLAY = True
    while True:
        playagain_ = input("WOULD YOU LIKE TO PLAY AGAIN? Y/N").lower()

        if playagain_ == 'n': # Ends the program.
            REPLAY = False
            break
        elif playagain_ == 'y':
            REPLAY = True
            break
        else:
            print('\nInvalid input...')

    if REPLAY == True:
        pass
    if REPLAY == False:
        break
