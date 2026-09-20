# import string
# alphabet = list(string.ascii_lowercase)   

from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount): # 'abc', 3
    shifted_text = ""
    for char in original_text: # a
        shifted_position =  alphabet.index(char) + shift_amount
        shifted_position %= len(alphabet)
        shifted_text += alphabet[shifted_position]
    print(f"Here is the encoded result : {shifted_text}") 
    # def

# encrypt(original_text=text, shift_amount=shift)

def decrypt(original_text, shift_amount): # def , 3  : o/p --> abc
     output_text = ""
     for char in original_text:
         shifted_position = alphabet.index(char) - shift_amount
         shifted_position %= len(alphabet)
         output_text += alphabet[shifted_position]
     print(f"Here is the decoded result : {output_text}")

# decrypt(original_text=text, shift_amount=shift)

def caesar(user_direction):
    if user_direction == 'encode':
        encrypt(text, shift)
    elif user_direction == 'decode':
        decrypt(text, shift)
    else:
        print("Invalid input")

caesar(direction)


