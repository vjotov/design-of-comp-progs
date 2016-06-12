# 1 There are five houses.
# 2 The Englishman lives in the red house.
# 3 The Spaniard owns the dog.
# 4 Coffee is drunk in the green house.
# 5 The Ukrainian drinks tea.
# 6 The green house is immediately to the right of the ivory house.
# 7 The Old Gold smoker owns snails.
# 8 Kools are smoked in the yellow house.
# 9 Milk is drunk in the middle house.
# 10 The Norwegian lives in the first house.
# 11 The man who smokes Chesterfields lives in the house next to the man with the fox.
# 12 Kools are smoked in a house next to the house where the horse is kept.
# 13 The Lucky Strike smoker drinks orange juice.
# 14 The Japanese smokes Parliaments.
# 15 The Norwegian lives next to the blue house.
# Who drinks water? Who owns the zebra?

import itertools

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))

#2
def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1
    
def nextto(h1, h2) :
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1 #question here


#1
for (red, green, ivory, yellow, blue) in orderings:
    for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings:
        for (dog, snails, fox, horse, ZEBRA) in orderings:
            for (coffee, tea, milk, oj, WATER) in orderings:
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
                    # constraints go here
                    if (Englishman == red) : #2
                    #if (Englishman is red)
                    
                    
#3
def zebra_puzzle():
    "Returns a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) #1
    return next((WATER, ZZEBRA)
        for (red, green, ivory, yellow, blue) in orderings:
        for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings:
        for (dog, snails, fox, horse, ZEBRA) in orderings:
        for (coffee, tea, milk, oj, WATER) in orderings:
        for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
        if Englishman is red            #2
        if Spaniard is dog              #3
        if coffee is green              #4
        if Ukrainian is tea             #5
        if imright(green, ivory)        #6
        if OldGold is snails            #7
        if Kools is yellow              #8
        if milk is middle               #9
        if Norwegian is first           #10
        if nextto(Chesterfields, fox)   #11
        if nextto(Kools, horse)         #12
        if LuckyStrike is oj            #13
        if Japanese is Parliaments      #14
        if nextto(Norwegian, blue)      #15
        )
        
#4 
def zebra_puzzle2():
    "Returns a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) #1
    return next((WATER, ZZEBRA)
        for (red, green, ivory, yellow, blue) in orderings:
        if imright(green, ivory)        #6
        for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings:
        if Englishman is red            #2    
        if Norwegian is first           #10
        if nextto(Norwegian, blue)      #15
        for (coffee, tea, milk, oj, WATER) in orderings:
        if coffee is green              #4 
        if Ukrainian is tea             #5
        if milk is middle               #9
        for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
        if Kools is yellow              #8    
        if LuckyStrike is oj            #13
        if Japanese is Parliaments      #14
        for (dog, snails, fox, horse, ZEBRA) in orderings:
        if Spaniard is dog              #3
        if OldGold is snails            #7
        if nextto(Chesterfields, fox)   #11
        if nextto(Kools, horse)         #12
        )
        
        
# Timed Calls
def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result
    
def timedcalls(n, fn, *args):
    "Call function n times with args; return min, avg, and max time."
    times = [timecall(fn, *ergs)[0] for _ in range(n)]
    return min(times), average(times), max(times)

def average(numbers):
    "return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))
    