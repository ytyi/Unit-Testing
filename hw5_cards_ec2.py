import hw5_cards as hw
import copy
class Hand:
    '''a hand for playing card
    Class Attributes
    ----------------
    None
    Instance Attributes
    -------------------
    init_card: list
    a list of cards
    '''
    def __init__(self, init_cards):
        self.init_card=init_cards
    def add_card(self, card):
        '''add a card
        add a card to the hand
        silently fails if the card is already in the hand
        Parameters
        -------------------
        card: instance
        a card to add
        Returns
        -------
        None
        '''
        if card in self.init_card:
            pass
        else:
            self.init_card.append(card)
    def remove_card(self, card):
        '''remove a card from the hand
        Parameters
        -------------------
        card: instance
        a card to remove
        Returns
        -------
        the card, or None if the card was not in the Hand
        '''
        if card in self.init_card:
            self.init_card.remove(card)
            return card
        else:
            return None


    def draw(self, deck):
        '''draw a card
        draw a card from a deck and add it to the hand
        side effect: the deck will be depleted by one card
        Parameters
        -------------------
        deck: instance
        a deck from which to draw
        Returns
        -------
        None
        '''
        self.init_card.append(deck.deal_card())

    def remove_pairs(self):
        '''draw a card
        remove pairs of cards
        side effect: the deck will be depleted by one card
        Parameters
        -------------------
        None
        Returns
        -------
        None
        '''
        list_delete=[]
        i=len(self.init_card)-1
        while(i>0):
            j=i-1
            while(j>=0):
                if self.init_card[i].rank==self.init_card[j].rank:
                    del self.init_card[i]
                    del self.init_card[j]
                    i=i-1
                    break
                else:
                    j=j-1
            i=i-1


