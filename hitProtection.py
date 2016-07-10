
import sys

if len(sys.argv) == 1:
    print('no possible positions given!')
    exit(1)

def printStat(position, probability):

    print("%d space(s) away from a enemy checker has an approximately %d%% chance of getting hit" % (position,probability))

dieOne = [1,2,3,4,5,6]
dieTwo = [1,2,3,4,5,6]

universeSize = float(len(dieOne) * len(dieTwo))

valueOccurances = [0] * 12

# Calculate the number of occurences for all possible positions
for dieOneCurrentValue in dieOne:
    for dieTwoCurrentValue in dieTwo:
        valueOccurances[dieOneCurrentValue  - 1] += 1 
        if dieOneCurrentValue != dieTwoCurrentValue:
            valueOccurances[dieTwoCurrentValue  - 1] += 1 
        diceSum = dieOneCurrentValue  + dieTwoCurrentValue
        valueOccurances[diceSum - 1] += 1 

for proposedPosition in sys.argv[1:]:

    try:

        if int(proposedPosition) < 1:
            print('too small')
            continue

    except ValueError:

        print("invalid integer given %s" % proposedPosition )
        continue

    proposedPosition = int(proposedPosition)

    if proposedPosition <= 12:

        percentage = int((float(valueOccurances[proposedPosition-1])/universeSize) * 100.0)

    else:
        
        percentage = 0

    printStat(proposedPosition,percentage) 





