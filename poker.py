import random

#1
def poker(hands):
    "Returns the list of wining hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)
#9
def allmax(iterable, key=None):
    "Returns a list of all items equal to the max of the iterable"
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x]
        elif xval == maxval:
            result.append(x)
    return result

#2
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # stright flush  # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9h 9S 9C 7D".split() # four of a kind
    fh = "TD TC TH 7C 7D".split() # full house
    tp = "5S 5D 9H 9C 6S".split() # two pairs
    s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
    s2 = "2C 3C 4C 5S 6S".split() # 2-6 straight <-
    ah = "AS 2S 3S 4S 6C".split() # A high
    sh = "2S 3S 4S 6C 7D".split() # 7 high
    assert poker([s1, s2, ah, sh]) == s2
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5)
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf,fk,fh]) == sf
    assert poker([fh, fk]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return "test pass"
    
#3
def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3,ranks), kind(2, ranks))  # your code here
    elif flush(hand):                              # flush
        return (5, ranks)               # your code here
    elif straight(ranks):                          # straight
        return (4, max(ranks))               # your code here
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks) # your code here
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks) # your code here
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks),ranks)# your code here
    else:                                          # high card
        return (0, ranks) # your code here
#12 refactoring
def new_hand_rank(hand):
    "Returns a value indicating how high the hand ranks," 
    # counts in the count of each rank; ranks lists corresponding card_ranks
    # E.g '7 T 7 9 7' => counts (3, 1, 1); ranks = (7, 10, 9)
    groups = group(['--23456789TJQKA'.index(r) for r,,s in hand])
    counts, ranks = unzip(groups
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r,s in hand]) == 1
    return (9 if (5,) == counts else
            8 if straught and flush else
            7 if (4, 1) == counts else
            6 if (3, 2) == counts else
            5 if (flush) else
            4 if straight else
            3 if (3, 1, 1) == counts else
            2 if (2, 2, 1) == counts else
            1 if (2, 1, 1, 1) == counts else
            0), ranks
#13
def group(items):
    "Return a list of [(count,x)...], highest count first, then highest x first."
    groups = [(items.count(x), x for x in set(items)]
    return sorted(groups, reverse=True)
    
#14 
def new2_hand_rank(hand):
    "Returns a value indicating how high the hand ranks," 
    # counts in the count of each rank; ranks lists corresponding card_ranks
    # E.g '7 T 7 9 7' => counts (3, 1, 1); ranks = (7, 10, 9)
    groups = group(['--23456789TJQKA'.index(r) for r,,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r,s in hand]) == 1
    return max(count_ranking[counts], 4* straight + 5*flush), ranks
    
count_rankings = {(5,):10, (4,1):7, (3, 2):6, (3, 1, 1):3, (2, 2, 1):2,
                 (2, 1, 1, 1):1, (1, 1, 1, 1, 1):0}    
    
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens 
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function 
#                  returns their corresponding ranks as a 
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks 
#                  in a hand (where the order goes from
#                  highest to lowest rank). 
#
# Since we are assuming that some functions are already
# written, this code will not RUN. Clicking SUBMIT will 
# tell you if you are correct.

#4
def card_ranks(hand):
    "Return a list of ranks, sorted with higher first."
    ranks = ["--23456789TJQKA".index(r) for r, s in hand]
    ranks.sort(reverse=True)
#8  return ranks -> 
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks 
    

#5
def straight(ranks):
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5
    
def flush(hand):     
    suits = [s for r, s in hand]
    return len(set(suits)) == 1
    
#6
def kind(n, ranks):
#    """ Returns the first rank that this hand has exactly n of.
#    Returns None if there is no n-of-a-kind in the hand."""
#    return None
    l = [0] * 15
    for i in ranks:
        l[i] = l[i]+1
    for i, e in reversed(list(enumerate(l))):
        if e == n:
            return i
    return None
    ##### from the udacity
    # for r in ranks:
    #   if ranks.count(r) == n: return r
    # return None

#7   
def two_pair(ranks):
    l = [0] * 15
    answers = [0] * 2
    for i in ranks:
        l[i] = l[i]+1
    for i, e in reversed(list(enumerate(l))):
        if e == 2:
            if answers[0] == 0:
                answers[0] = i
            else:
                answers[1] = i
    if answers[0] == 0 or answers[1] == 0:
        return None
    else:
        return (answers[0], answers[1])
##### from the udacity
    # pair = kind(2, ranks)
    # lowpair = kind(2, list(reversed(ranks)))
    # if pair and lowpair != pair:
    #   return (pair, lowpair)
    # else: 
    #   return None

#8 handle A2345 as straight

#9 handle ties

#10 deal - quiz
def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    "Shuffle the deck and deal out numhands n-card hands."
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
    
#11 - hand frequencies
def hand_percentages(n=700*1000):
    "Sample n random hands and print a table of percentages for each type of hand.
    counts = [0]*9
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print "%14s: %6.3f %%" % (hand_names[i], 100.*counts[i]/n)
        

print test()


#sf = "6C 7C 8C 9C TC".split()
#print hand_rank(sf)
#print straight([9, 8, 7, 6, 5])
#fk = "TD TC TH 7C 7D".split()
#fkranks = card_ranks(fk)
#print two_pair(fkranks)

#print kind(2, fkranks) 
#print kind(1, fkranks) 

#print fkranks
#l = [0] * 15
#for i in fkranks:
#    l[i] = l[i]+1
#for i, e in reversed(list(enumerate(l))):
#    print i, e
#print max(l)

#rates = map(fkranks.count(r), r in fkranks)
#print rates
#print map(range(8))

