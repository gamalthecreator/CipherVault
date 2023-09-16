

MORSE_CODE_DICT= {'A': '.-', 'B': '-...',  'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-','L': '.-..', 'M': '--', 'N': '-.','O': '---', 'P': '.--.', 'Q': '--.-',
                'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--','X': '-..-', 'Y': '-.--', 'Z': '--..',
                '1': '.----', '2': '..---', '3': '...--','4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                '0': '-----', ', ': '--..--', '.': '.-.-.-','?': '..--..', '/': '-..-.', '-': '-....-','(': '-.--.', ')': '-.--.-','$/': ' ','\n': "   "}


def morse_code_cipher(cleartext):
    MORSE_CODE_DICT= {'A': '.-', 'B': '-...',  'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-','L': '.-..', 'M': '--', 'N': '-.','O': '---', 'P': '.--.', 'Q': '--.-',
                'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--','X': '-..-', 'Y': '-.--', 'Z': '--..',
                '1': '.----', '2': '..---', '3': '...--','4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                '0': '-----', ', ': '--..--', '.': '.-.-.-','?': '..--..', '/': '-..-.', '-': '-....-','(': '-.--.', ')': '-.--.-'}


    message= cleartext.upper()
    encrypted_message=[]

    for c in message:
        if c in MORSE_CODE_DICT:
            encrypted_message.append(MORSE_CODE_DICT[c] + ' ')
        elif c == '\n':
            encrypted_message.append('\n')
        else:
            encrypted_message.append(' ')
    encrypted_message= "".join(encrypted_message)

    return encrypted_message


def morse_code_decipher(ciphered_message):
    MORSE_CODE_DICT_INV= {v: k for k, v in MORSE_CODE_DICT.items()}

    encrypted_message= ciphered_message

    morse_words= encrypted_message.split()

    decrypted_message= ""
    for morse_word in morse_words:
        decrypted_message += MORSE_CODE_DICT_INV.get(morse_word, " ")

    return decrypted_message

