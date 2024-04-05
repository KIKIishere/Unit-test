import unittest
import cards
from cards import Card, Deck

class TestCard(unittest.TestCase):

    def test_q1(self):
        """Test creating a card with rank 12, its rank_name will be 'Queen'."""
        card = Card(suit=1, rank=12)
        return (card.rank_name, "Queen")
    
    def test_q2(self):
        """Test creating a card instance with suit 1, its suit_name will be 'Clubs'."""
        card = Card(suit=1, rank=3)
        return (card.suit_name, "Clubs")
    


    def test_q3(self):
        """Test the str representation of a card with suit=3 and rank=13."""
        card = Card(suit=3, rank=13)
        return (str(card), "King of Spades")
    
    def test_q4(self):
        """Test creating a Deck instance results in 52 cards."""
        deck = Deck()
        return (len(deck.cards), 52)

    def test_q5(self):
        """Test dealing a card from the deck returns a Card instance."""
        deck = Deck()
        card = deck.deal_card()
        # Return a tuple with the dealt card as its only element
        return (card,)

    def test_q6(self):
        """Test the deck size decreases by one after dealing a card."""
        deck = Deck()
        initial_size = len(deck.cards)
        deck.deal_card()
        return (len(deck.cards), initial_size - 1)


    def test_q7(self):
        """Test the deck size increases by one after replacing a dealt card."""
        deck = Deck()
        card = deck.deal_card()
        initial_size = len(deck.cards)
        deck.replace_card(card)
        return (len(deck.cards), initial_size + 1)

    def test_q8(self):
        """Test the deck size remains unchanged when trying to replace a card that's already in the deck."""
        deck = Deck()
        card = deck.cards[0]  # Assume this card is still in the deck
        initial_size = len(deck.cards)
        deck.replace_card(card)  # Try to replace a card that's already in the deck
        return (len(deck.cards), initial_size)


if __name__=="__main__":
    unittest.main()