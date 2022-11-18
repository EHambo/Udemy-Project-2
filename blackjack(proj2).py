import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True #Controls main loop

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

# Functions
def take_bet(chips):

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
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
def hit_or_stand(deck,hand):

    global playing # to control an upcoming while loop
    playing = True

    while playing == True:

        userchoice_ = input("Hit or Stand?").capitalize()
        print(userchoice_)
        if userchoice_ == "Hit":
            print('we hit')
            hit(deck,hand)
        elif userchoice_ == "Stand":
            print('we stand')
            playing = False
        else:
            print("Invalid input...")
def show_some(player,dealer):

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

    for card_ in player.cards: print(card_)
    print(player.value)

    for card_ in dealer.cards: print(card_)
    print(dealer.value)
def player_busts():

    show_all(player,dealer)
    chips.lose_bet()
    print(f'You busted. {bet} in chips have been removed from your pot.')
    playing = False #Global var..
def player_wins():

    show_all(player,dealer)
    chips.win_bet()
    print(f'You Win! {bet} in chips have been added to your pot.')
    playing = False #Global var..
def dealer_busts():

    show_all(player,dealer)
    chips.win_bet()
    print(f'Dealer busted, and you win! {bet} in chips have been added to your pot.')
    playing = False #Global var..
def dealer_wins():
    show_all(player,dealer)
    chips.win_bet()
    print(f'Dealer wins. {bet} in chips have been removed from your pot.')
    playing = False #Global var..
def push():
    print('Game ends in a draw.')

# Main program
while True: #Could I do a while true then break it if player doesn't wish to play?
    print('Welcome to Blackjack!')

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
    player_chips = Chips()
    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    print(playing)
    while playing:  # recall this variable from our hit_or_stand function

        hit_or_stand(game_deck,player_hand)
        dealer_hand.add_card(game_deck.deal())
        show_some(player_hand,dealer_hand)

        break
break
        # Show cards (but keep one dealer card hidden)


        # If player's hand exceeds 21, run player_busts() and break out of loop


            #break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17


        # Show all cards

        # Run different winning scenarios


    # Inform Player of their chips total

    # Ask to play again

        #break
