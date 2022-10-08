# ESP

import string



def main():
    print('''
    1. Encrypt
    2. Decrypt
    ''')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    else:
        print('Invalid choice')
        
def encrypt():
    text = input('Enter the text: ')
    shift = int(input('Enter the shift: '))
    cipher_text = ''
    for letter in text:
        if letter in string.ascii_letters:
            cipher_text += chr(ord(letter) + shift)
        else:
            cipher_text += letter
    print(f'The encoded text is {cipher_text}')
    
def decrypt():
    text = input('Enter the text: ')
    shift = int(input('Enter the shift: '))
    plain_text = ''
    for letter in text:
        if letter in string.ascii_letters:
            plain_text += chr(ord(letter) - shift)
        else:
            plain_text += letter
    print(f'The decoded text is {plain_text}')
    
if __name__ == '__main__':
    main()
    
