# Check for equality betwwn hash converter dictionaries
import sys
sys.path.append("..")

# Importing the Dictionaries
from hashes import getL, getN, getS

# Check for equality within all dicts
ltoh = getL()
ntoh = getN()
stoh = getS()

# Just for testing
d_test = {'s': 'efef',
          'f': 'fsdfd',
          'g': 'efef',
          'h': 'fsdfsdd',}

d2_test = {'q': 'sdfsdsdf',
           'w': '23432g',
           'r': 'sdfdsfsdfsdfsdf',
           't': 'fsdfd',}

d3_test = {'y': 'sdff',
           'p': 'sdfsdfsfdpp',
           'd': 'fsdfd'}

def newFlipped(hmap, flipped=None):
    # Store reversed k - v pairs
    if flipped is None:
        flipped = {}
    for k, v in hmap.items():
        if v not in flipped:
            flipped[v] = [k]
        else:
            flipped[v].append(k)
    return flipped


def selfCheck(hmap):
    # Check equality within one dictionary by reversing it
    flipped = newFlipped(hmap)
    return [v for k, v in flipped.items() if len(v) > 1]

def twoMapCheck(hmap_one, hmap_two, hmap_three):
    # Check for equal values in two dictionaries
    flipped = newFlipped(hmap_one) # Start reversed map with first dict
    flipped = newFlipped(hmap_two, flipped) # Add new hmap to flipped dict
    flipped = newFlipped(hmap_three, flipped) # Adding last hash map
    
    return [v for k, v in flipped.items() if len(v) > 1]


def print_dicts():
    # Simple print to get all info
    print('---ltoh---')
    for v, k in ltoh.items():
        print(f'{v} -> {k}')
    print('---ntoh---')
    for v, k in ntoh.items():
        print(f'{v} -> {k}')
    print('---stoh---')
    for v, k in stoh.items():
        print(f'{v} -> {k}')


def main():
    
    print_dicts()
    # Self checks for all values in maps
    print('---Self for ltoh---')
    print(selfCheck(ltoh))
    print('---Self for ntoh---')
    print(selfCheck(ntoh))
    print('---Self for stoh---')
    print(selfCheck(stoh))
        
    # Checking for duplicates within all maps
    print('--- Check for ltoh - ntoh - stoh ---')
    print(twoMapCheck(ltoh, ntoh, stoh))
    

    # Debugging - Test Cases
    #print(selfCheck(d_test))
    #print(twoMapCheck(d_test, d2_test, d3_test))


if __name__ == '__main__':
    main()


