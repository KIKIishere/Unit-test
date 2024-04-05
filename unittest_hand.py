# unittest_hand.py
import unittest
from hand import Hand
from cards import Card, Deck

class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand([Card(2, 3), Card(3, 3)])  # A hand with 2 of Diamonds and 3 of Diamonds

    def test_hand_initialization(self):
        self.assertEqual(len(self.hand.cards), 2)

    def test_add_and_remove_card(self):
    # Assuming 2 is the correct index for Clubs
        new_card = Card(2, 4)  # Correctly add 4 of Clubs
        self.hand.add_card(new_card)
        self.assertIn(new_card, self.hand.cards, "4 of Clubs was not added correctly.")
        self.hand.remove_card(new_card)
        self.assertNotIn(new_card, self.hand.cards, "4 of Clubs was not removed correctly.")


    # def test_draw(self):
    #     deck = Deck()
    #     self.hand.draw(deck)
    #     self.assertEqual(len(self.hand.cards), 3)

    def test_draw_from_deck(self):
        """Test drawing a card from a deck adds to hand."""
        deck = Deck()
        initial_deck_size = len(deck.cards)
        self.hand.draw(deck)
        self.assertEqual(len(self.hand.cards), 3, "Card was not drawn correctly into the hand.")
        self.assertEqual(len(deck.cards), initial_deck_size - 1, "Deck size did not decrease.")

    def remove_pairs(self):
        # Create a dictionary to count occurrences of each rank
        rank_counts = {}
        for card in self.cards:
            if card.rank in rank_counts:
                rank_counts[card.rank] += 1
            else:
                rank_counts[card.rank] = 1
        
        # Identify ranks that have pairs (even counts) and remove two for each pair
        for rank, count in rank_counts.items():
            while count >= 2:
                # Remove two cards of this rank from the hand for each pair
                cards_removed = 0
                for card in list(self.cards):  # Use list() to create a copy for safe iteration
                    if card.rank == rank and cards_removed < 2:
                        self.cards.remove(card)
                        cards_removed += 1
                count -= 2
# Write more tests...

if __name__ == '__main__':
    unittest.main()
