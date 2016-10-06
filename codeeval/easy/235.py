import sys

cards_order = {'1':10, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'J':11,
               'Q':12, 'K':13, 'A':14}


def select_max_cards(cards_deck):
    d = { cards_order[card[0]]:card[0] for card in cards_deck }
    max_card = d[max(d.keys())]
    win = [ c for c in cards_deck if c[0] == max_card ]
    return win


with open(sys.argv[1]) as f:
    for line in f:
        cards, trump_suite = line.strip().split(' | ')
        cards = cards.split()
        trump_cards = [i for i in cards if i[-1] == trump_suite]
        if len(trump_cards) == 0 or len(trump_cards) == len(cards):
            cards_win = select_max_cards(cards)
            print ' '.join(cards_win)
        else:
            if len(trump_cards) == 1:
                print trump_cards[0]
            else:
                cards_win = select_max_cards(trump_cards)
                print ' '.join(cards_win)

