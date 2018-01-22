import random

def play_blackjack(draw_if_less_than):

    deck = []
    hand = []
    dealer = []
    handTotal = 0
    handDealer = 0

    # Create single-digit cards
    for i in range(2, 10):
    	a = i
    	deck.append(a)

    # Create 10 cards
    count_1 = 16
    while count_1 > 0:
    	deck.append(10)
    	count_1 -= 1

    # Create aces
    count_2 = 4
    while count_2 > 0:
    	deck.append(11)
    	count_2 -= 1

    # Set up 2 hand for yourself
    while len(hand) < 2:
    	drawCard = random.choice(deck)
    	hand.append(drawCard)
    	deck.remove(drawCard)
    	handTotal += drawCard

    # Set up 2 hand for the dealer
    while len(dealer) < 2:
    	drawCard = random.choice(deck)
    	dealer.append(drawCard)
    	deck.remove(drawCard)
    	handDealer += drawCard

    # Hit or stand descision
    while handTotal < draw_if_less_than:
        drawCard = random.choice(deck)
        hand.append(drawCard)
        deck.remove(drawCard)
        handTotal += drawCard
        print(hand)

    # Dealer moves <stands on all +17>
    while handDealer <= 17:
        drawCard = random.choice(deck)
        dealer.append(drawCard)
        deck.remove(drawCard)
        handDealer += drawCard
        print(dealer)

    print(handTotal)
    print(handDealer)
