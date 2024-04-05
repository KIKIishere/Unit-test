# create the Hand with an initial set of cards
from cards import Card, Deck

class Hand:
    '''A hand for playing card.'''

    def __init__(self, card_list=None):
        # Use a default mutable argument safely
        if card_list is None:
            card_list = []
        self.cards = card_list

    def add_card(self, card):
        # Check if the card is not already in the hand before adding
        if card not in self.cards:
            self.cards.append(card)

    def remove_card(self, card):
        # Remove the card if it's in the hand, otherwise do nothing
        try:
            self.cards.remove(card)
            return card
        except ValueError:
            return None

    def draw(self, deck):
        # Draw a card from the deck if it's not empty
        if isinstance(deck, Deck) and len(deck.cards) > 0:
            card = deck.deal_card()
            self.add_card(card)

    def remove_pairs(self):
        # Correctly remove all pairs from the hand
        ranks_with_pairs = set()
        for card in self.cards:
            if self.cards.count(card) >= 2:
                ranks_with_pairs.add(card.rank)
        
        # Remove the pairs
        self.cards = [card for card in self.cards if card.rank not in ranks_with_pairs or ranks_with_pairs.remove(card.rank)]

# class Hand:
#     '''a hand for playing card '''


#     def __init__(self, card_list=[]):
#         self.cards = card_list

        
#         '''

#         init the hand instance

#         Parameters
#         -------------------
#         init_cards: a list of card instance
#         the instance should be created using the card class in card.py

        
#         Attributes
#         -------------------
#         cards: list
#         use the init_cards to create self.cards
#         a list of cards instance, indicating the cards in the hand
        

#         '''



#     def add_card(self, card):
#         self.cards.append(card)

#         '''
        
#         add a card to hand
#         silently fails if the card is already in the hand
#         assuming there is only one deck with 52 cards (except jokers)
#         two different cards instance with the same rank and suit are 
#         regarded as one card
        
#         for example:
#             card1 = Card(suit=0,rank=2)
#             card2 = Card(suit=0,rank=2)
#             card1 and card2 are regarded as the same card

#         Parameters
#         -------------------
#         card: card instance
#         a card to add

#         Returns
#         -------
#         None

#         ''' 


#     def remove_card(self, card):
#         self.cards.remove(card)
#         '''

#         remove a card from the hand

#         Parameters
#         -------------------
#         card: card instance
#         a card to remove

#         Returns
#         -------
#         the removed card instance, or None if the card was not in the Hand

#         '''


#     def draw(self, deck):
#         card = deck.deal_card()
#         if card:
#             self.cards.append(card)
#         '''

#         draw a card from a deck and add it to the hand
#         side effect: the deck will be depleted by one card

#         Parameters
#         -------------------
#         deck: deck instance
#         a deck from which to draw
        
#         Returns
#         -------
#         None

#         '''
    
#     def remove_pairs(self):
#         '''

#         remove all the pairs in the hand
#         this method is for extra credit 2
        
#         Parameters
#         -------------------
#         None
        
#         Returns
#         -------
#         None

#         '''
#         counts = {}
#         for card in self.cards:
#             counts[card.rank] = counts.get(card.rank, 0) + 1

#         for rank, count in counts.items():
#             while count > 1:
#                 self.cards = [card for card in self.cards if card.rank != rank or count <= 1]
#                 count -= 2 if count > 2 else count