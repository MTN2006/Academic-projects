#user defined function to read file as a list
def read_deck(filename:str)-> list:
    deck=[]
    #opens file 
    with open(filename,'r') as file:
        for line in file:
            card=line.strip()
            #checks if it is an empty string and takes out joker fromd deck
            if card and 'Joker' not in card:
                deck.append(card)
        return deck

def shuffle(deck: list):
    #splits the deck into two parts
    middle = len(deck) // 2
    #index to represent right and left side of deck
    rhs = deck[middle:]
    lhs = deck[:middle]

    shuffled_deck = []

    # Interleave the cards correctly
    for left_card, right_card in zip(lhs, rhs):
        shuffled_deck.append(left_card)
        shuffled_deck.append(right_card)

    # Handle the case where the deck has an odd number of cards
    if len(deck) % 2 != 0:
        shuffled_deck.append(lhs[-1])  # Add the last card from the left half

    return shuffled_deck  # Return the shuffled deck


def deal_card(shuffled_deck:list, number_of_cards:int):
    if number_of_cards<= number_of_cards:
        if number_of_cards==1:
            return shuffled_deck.pop()
        if number_of_cards>1:
            dealt_cards=[]
        for _ in range(number_of_cards):
               dealt_cards.append(shuffled_deck.pop())
        return dealt_cards
    else:
        return None

def card_value(card):
    # Assuming card format is something like "Ace of Spades", "10 of Hearts", etc.
    value = card.split(' ')[0]  # Get the rank of the card (e.g., "Ace", "10", "King")

    # Check for face cards and Ace
    if value == 'Ace':
        return 11  # Ace is worth 11 points
    elif value in ['King', 'Queen', 'Jack']:
        return 10  # King, Queen, and Jack are worth 10 points

    # If it's a number card (like "2", "3", etc.), convert it to an integer
    return int(value)


def hand_value(hand):
    # Calculate the total value of the hand by summing up the card values
    total_value = 0
    for card in hand:
        total_value += card_value(card)
    return total_value


def blackjack(hand_value: list):
    # Check if the hand is a blackjack (Ace + 10-value card)
    if len(hand_value) == 2:
        card_values = [card_value(card) for card in hand_value]
        return 11 in card_values and 10 in card_values
    return False


def should_hit(hand: list):
    # Suggest hitting if hand value is less than 17
    total_value = hand_value(hand)
    return total_value < 17


def play_hand(hand: list, shuffled_deck: list):
    # Keep dealing cards until the hand reaches a value of 17 or more
    while should_hit(hand) and len(shuffled_deck) > 0:
        hand.append(deal_card(shuffled_deck, 1))


def compare_hands(agent_hand, dealer_hand):
    agent_value = hand_value(agent_hand)
    dealer_value = hand_value(dealer_hand)

    # Determine the result based on hand values and busts
    if agent_value > 21:
        return "Player busts!"
    elif dealer_value > 21:
        return "Dealer busts!"
    elif agent_value > dealer_value:
        return "Player wins!"
    elif dealer_value > agent_value:
        return "Dealer wins!"
    else:
        return "Push!"


    
def main():
    # Prompt the user to enter the filename
    filename = input('Enter filename: ')  
    
    # Read the deck from the file
    deck_of_cards = read_deck(filename)  
    
    # Shuffle the deck
    shuffled_deck = shuffle(deck_of_cards)  
    
    # Play the game until the number of cards left in the deck is less than or equal to 10
    while len(shuffled_deck) > 10:
        # Initialization: Deal initial hands to the agent and dealer (2 cards each)
        agent_hand = deal_card(shuffled_deck, 2)
        dealer_hand = deal_card(shuffled_deck, 2)

        # Play the agent's hand
        play_hand(agent_hand, shuffled_deck)
        
        # Play the dealer's hand
        play_hand(dealer_hand, shuffled_deck)
        
        # Compare the hands and get the result
        result = compare_hands(agent_hand, dealer_hand)
        
        # Print the result of the comparison
        print(result)



 

if __name__ == "__main__":
    main()


