from wsgiref.util import shift_path_info




def encode(original_text, shifted_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet_list.index(letter) + shifted_amount
        shifted_position %= len(alphabet_list)
        cipher_text = cipher_text + alphabet_list[shifted_position]
    print(f'Your encoded result is : {cipher_text}')


encode(original_text=text, shifted_amount=shift)

