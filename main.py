from hashes.letter import getL, getHtoL
from hashes.number import getN, getHtoN
from hashes.symbol import getS, getHtoS
from encoders.encode import encodeM
from encoders.decode import decodeM
from xhash import XHash

def tester():
    myp = 'sdGUh//8$%/¿¿?¡'
    print(f'This is myp: {myp}')
    print('---- coded ----')
    newcoded = encodeM(myp, getL(), getN(), getS())
    print(newcoded)
    print('---- decoded ----')
    decoded = decodeM(newcoded, getHtoL(), getHtoN(), getHtoS())
    print(''.join(decoded))
    print(myp == ''.join(decoded))

def addPWD():
    name = input('Name:  ')
    username = input('Username:  ')
    pwd = input('Pwd:  ')
    coded = encodeM(pwd, getL(), getN(), getS())
    newPWD = XHash(name, username, pwd, coded)
    #print(newPWD)
    try:
        newPWD.saveToDB()
        print('*** Saved Correctly ***')
    except:
        print("Error Saving")

def intro():
    print('******** xHash Manager *******')
    enter_code = input('Enter code: ')
    counter = 0
    while (enter_code != 'wolf'):
        if counter == 2:
            print('******** Access Denied *******\nExiting...')
            exit()
        enter_code = input('Enter code: ')
        counter += 1
    print('******** Access Granted *******\n')

def getPWD():
    name = input('Name of the program: ')
    # check if name is in the db
    # algorithm to search for similar words

def main():
    intro()
    action = 0
    while (action != 1 and action != 2):
        try:
            action = int(input('1- Add new pwd\n2- Get pwd\n'))
            if action == 1:
                addPWD()
            elif action == 2:
                getPWD()
            else:
                print('Enter a correct option')
        except ValueError:
            print('Enter a correct option')
        
    
    
if __name__ == '__main__':
    main()


