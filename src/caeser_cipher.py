import CipherVault
import enchant

def caeser_encrypt(message, shiftValue):
    return CipherVault.shift_text(message, shiftValue)


def caeserCipher(message, programType):
    if programType == 'E':
        while True:
            try:
                shiftVal = int(input("Please enter the shift value (Only integer): "))
                break
            except ValueError:
                print("That is not an integer. Please try again.")
    else:
        while True:
            key = input("Got the key? (Y or N)")
            if key == 'Y':
                while True:
                    try:
                        shiftVal = int(input("Please enter the shift value (Only integer): "))
                        break
                    except ValueError:
                        print("That is not an integer. Please try again.")
                break
            elif key == 'N':
                return automatic_caeser_decipher(message)
            else:
                print("Wrong input. Please try again.")
                
        shiftVal = shiftVal * -1
    return CipherVault.shift_text(message,shiftVal)


def automatic_caeser_decipher(message):
    
    d = enchant.Dict("en_US")
    bestScore = 0
    bestShift = 0
    multipleScore = []
    multipleShifts = []
    for shift in range(1,26):
        score = 0
        shiftedMessage = CipherVault.shift_text(message,shift).split()
        for word in shiftedMessage:
            if d.check(word):
                score +=1
        
        if score > bestScore:
            bestScore = score
            bestShift = shift
            multipleScore.append([shift, score])
        elif score == bestScore and bestScore != 0:
            multipleScore.append([shift, score])
    if len(multipleScore) > 0:
        for scoreList in multipleScore:
            if scoreList[1] >= bestScore:
                multipleShifts.append("\'" + (CipherVault.shift_text(message, scoreList[0])) + "\', shifting: " + str(scoreList[0]))
        return multipleShifts
    else:
        shift_value = 26 - bestShift
        return (CipherVault.shift_text(message, bestShift)), (shift_value)
