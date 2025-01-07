



def caesar(user_letter, shift_amount, encode_or_decode):
    cipher_text = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for char in user_letter:
        if char not in alphabet_list:
            cipher_text += char
        else:
            
            
            total_shift = alphabet_list.index(char) + shift_amount
            total_shift = total_shift % len(alphabet_list)
            cipher_text += alphabet_list[total_shift]
    print(f'You {encode_or_decode}d letter is : {cipher_text}')
    
should_continue = True
while should_continue:
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    
    direction = input("Type 'encode' to encrypt, type 'decode' to 'decrypt' :  ").lower()
    text = input("Type your letter : ").lower()
    shift = int(input("Type the shift number : "))

    caesar(user_letter=text, shift_amount=shift, encode_or_decode=direction)
    result= input("Type 'yes' if you want to go again. Othewise, type 'no'. : ").lower()
    if result=="no":
        should_continue = False
        print("Good Bye...")
    
    