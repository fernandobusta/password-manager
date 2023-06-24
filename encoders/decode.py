

# Dict Checker
def isItHere(snip, pmap): 
    # Check if the snipped coded is in the given map
    
    # Check if it is a capital letter: '__' before the code
    if snip[:2] == '__':
        return snip[2:] in pmap
    return snip in pmap
    


def decodeM(coded, ltoh, ntoh, stoh):
    decoded = []

    # Iterate through the coded hash
    for ch in coded:
        # =============== Letter  =============
        if isItHere(ch, ltoh) is True:
            # Check if it is capital: '__'
            if ch[:2] == '__':
                decoded.append(ltoh[ch[2:]].upper())
            #decoded.append()
            else:
                decoded.append(ltoh[ch])
        # =============== Digit =============
        elif isItHere(ch, ntoh) is True:
            decoded.append(ntoh[ch])
        # =============== Symbol  =============
        elif isItHere(ch, stoh) is True:
            decoded.append(stoh[ch])
        # =============== Undefined  =============
        else:
            print(f'{ch} does NOT exist in hashes')

    return decoded
    






# TODO: Add main() if name -> manually decode a pwd inputed from CLI
