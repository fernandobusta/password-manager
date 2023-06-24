
def encodeM(pwd, ltoh, ntoh, stoh):
    # return string with coded message
    coded = []
    
    for ch in pwd.strip():
        # =============== Letter  =============
        if ch.isalpha(): # letter
            if ch.isupper(): # upper case
                try:
                    #print(f'{ch} - {ltoh[ch.lower()]}')
                    coded.append(f'__{ltoh[ch.lower()]}')
                except KeyError:
                    print(f'{ch} not in ltoh map')
            else: # lower case
                try:
                    #print(f'{ch} - {ltoh[ch]}')
                    coded.append(ltoh[ch])
                except KeyError:
                    print(f'{ch} not in ltoh map')
        # =============== Digit =============
        elif ch.isdigit():
            try:
                coded.append(ntoh[ch])
                #print(f'{ch} - {ntoh[ch]}')
            except KeyError:
                print(f'{ch} not in ntoh map')
        # =============== Symbol  =============
        else: # a symbol
            try:
                coded.append(stoh[ch])
                #print(f'{ch} - {stoh[ch]}')
            except KeyError:
                print(f'{ch} not in stoh map')
    print('\n**** passed test ****\n')
    
    return coded


# TODO: Create main() if name -> to manually imput pwd
