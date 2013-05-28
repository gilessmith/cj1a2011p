from codejam.utils.codejamrunner import CodeJamRunner
import codejam.utils.graphing as graphing
import networkx as nx

class Dynam(object):pass

def update_cards(deck, hand, card):
    new_hand = hand[:]
    new_hand.remove(card)
    new_hand += deck[0:card[0]]
    new_deck = deck[card[0]:]

    return new_hand, new_deck

def get_best_score(deck, hand, turn_count):

    if turn_count == 0  or len(hand) == 0:
        return 0

    for card in hand:
        if ((card[0] >0 or len(deck)== 0) and
            (card[2] >0 or len(deck) + len(hand) < turn_count)):

            new_hand, new_deck = update_cards(deck, hand, card)
            return card[1] + get_best_score(new_deck, new_hand, turn_count - 1 + card[2])

    # if we have reached here, then we have not found a neutral hand...
    # therefore iterate through all possible combinations

    t_max = max(hand, key=lambda j: j[2])
    c_max = max(hand, key=lambda j: j[0])

    c = c_max[0] + t_max[0]
    t = c_max[2] + t_max[2]
    if (c > 1 and t > 1) or (c>1 and turn_count > len(hand) + len(deck)) or (t > 1 and len(deck) ==0):
        new_hand, new_deck = update_cards(deck, hand, t_max)
        new_hand, new_deck = update_cards(new_deck, new_hand, c_max)

        return t_max[1] + c_max[1] + get_best_score(new_deck, new_hand, turn_count - 2 + c_max[2] + t_max[2])

    if t_max[2] == 0 and c_max[0] == 0:
        hand_by_score = sorted(hand[:], key=lambda card: -card[1])
        return sum([card[1] for card in hand_by_score[0:turn_count]])

    
    
    scores = []
    for card in hand:
        
        new_hand, new_deck = update_cards(deck, hand, card)
        scores.append(card[1] + get_best_score(new_deck, new_hand, turn_count - 1 + card[2]))

    return max(scores)



def solver(data):

    return get_best_score(data.deck, data.hand, 1)
    

  
def data_builder(f):

    data = Dynam()

    hand_len = f.get_int()

    data.hand = [f.get_ints() for i in range(hand_len)]

    deck_len = f.get_int()

    data.deck= [f.get_ints() for i in range(deck_len)]


    return data



cjr = CodeJamRunner()
cjr.run(data_builder, solver, problem_name = "C", problem_size='small-practice')
