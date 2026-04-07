def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print("=== Vigenere Cipher Tool ===")
print("1. Encrypt a message (Lock)")
print("2. Decrypt a message (Unlock)")
choice = input("Choose (1/2): ")

if choice in ['1', '2']:
    text = input('Enter the text: ')
    custom_key = input('Enter the key: ')

    if choice == '1':
        result = encrypt(text, custom_key)
        print(f'\nOriginal text: {text}')
        print(f'Encrypted result: {result}')
    else:
        result = decrypt(text, custom_key)
        print(f'\nCiphertext: {text}')
        print(f'Decrypted result: {result}')
else:
    print("Invalid choice!")