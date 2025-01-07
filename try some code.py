
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to 'decrypt' :  ").lower()
text = input("Type your letter : ").lower()
shift = int(input("Type the shift number : "))

def caesar(user_letter, shift_amount, encode_or_decode):
    
    cipher_text= ""
    for char in user_letter:
        if encode_or_decode== "decode":
            shift_amount *= -1
        total_shift=alphabet_list.index(char) + shift_amount
        total_shift = total_shift % len(alphabet_list)
        cipher_text += alphabet_list[total_shift]
    print(f'You {encode_or_decode}d letter is : {cipher_text}')

caesar(user_letter=text, shift_amount=shift, encode_or_decode=direction)