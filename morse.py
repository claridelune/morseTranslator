morse_dic = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
}
def get_key(val):
    for key, value in morse_dic.items():
         if val == value:
             return key

def encryption(message):
    message = message.lower()
    cipher_m = ''
    for letter in message:
        if letter != ' ':
            cipher_m += morse_dic[letter] + ' '
        else:
            cipher_m += ' '
    return cipher_m

def decryption(message):
    message += ' '
    decipher = ''
    letter = ''
    for char in message:
        if char != ' ':
            space = 0
            letter += char
        else:
            space += 1
            if space == 2:
                decipher += ' '
            else:
                letter = get_key(letter)
                decipher += str(letter)
                letter = ''
    return decipher

def main():
    choice = input("choose encryption or decryption?(e/d): ")
    outputMessage = ''
    if choice == 'e':
        inputMessage = input("Enter the text: ")
        outputMessage = encryption(inputMessage)
    elif choice == 'd':
        inputMessage = input("Enter the code: ")
        outputMessage = decryption(inputMessage)
    else:
        print("Invalid election")
    print(outputMessage)

if __name__ == '__main__':
    main()
