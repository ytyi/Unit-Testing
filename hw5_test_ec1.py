import unittest
import hw5_cards as hw5
import hw5_cards_ec1 as ec1

class TestHand(unittest.TestCase):
    def test_construct_Hand(self):
        deck=hw5.Deck()
        hand = ec1.Hand(deck.cards)
        self.assertEqual(len(hand.init_card),52)

    def testAddAndRemove(self):
        deck = hw5.Deck()
        card_missing=deck.deal_card()
        hand = ec1.Hand(deck.cards)
        for i in hand.init_card:
            hand.add_card(i)
            self.assertEqual(len(hand.init_card), 51)
        hand.add_card(card_missing)
        self.assertEqual(len(hand.init_card),52)

    def testdraw(self):
        deck = hw5.Deck()
        hand = ec1.Hand(deck.cards)
        deck1=hw5.Deck()
        hand.draw(deck1)
        self.assertEqual(len(hand.init_card),53)
        self.assertEqual(len(deck1.cards),51)

if __name__ == "__main__":
    unittest.main()