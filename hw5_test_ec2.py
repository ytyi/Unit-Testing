import unittest
import hw5_cards as hw5
import hw5_cards_ec2 as ec2

class TestHand(unittest.TestCase):

    def test_remove(self):
        card1=hw5.Card(1,5)
        card2=hw5.Card(2,5)
        card3 = hw5.Card(0, 5)
        card_list=[card1,card2,card3]
        hand=ec2.Hand(card_list)
        hand.remove_pairs()
        return self.assertEqual(len(hand.init_card),1)


if __name__ == "__main__":
    unittest.main()