from day_8_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)


def caesar(text, shift, direction):

    if direction == "encode":
        decode_text = ""
        
        for letter in text:
            # print(shift_index)
            # print(letter)

            if letter not in alphabet:
                decode_text += letter
                # print(decode_text)

            else:
                shift_index = alphabet.index(letter) + shift

                if shift_index >= len(alphabet):
                    new_shift_index = shift_index % len(alphabet)
                    # print(new_shift_index)
                    decode_text += alphabet[new_shift_index]
                    # decode_text.append(alphabet[new_shift_index])
                else:
                    decode_text += alphabet[shift_index]
                    # decode_text.append(alphabet[shift_index])


        print(f"The decoded text is {''.join(decode_text)}.")

    elif direction == "decode":
        encode_text = ""
        
        for letter in text:
            
            if letter not in alphabet:
                encode_text += letter
            else:
                shift_index = alphabet.index(letter) - shift

                if shift_index < 0:
                    new_shift_index = shift_index % len(alphabet)
                    # print(new_shift_index)
                    encode_text += alphabet[new_shift_index]
                    # decode_text.append(alphabet[new_shift_index])
                else:
                    encode_text += alphabet[shift_index]
                    # decode_text.append(alphabet[shift_index])
    
        print(f"The encoded text is {''.join(encode_text)}.")


acc_input = True
while acc_input is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if user_input == 'no':
        print("Bye.")
        acc_input = False

# =================================================================================================================
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char
#   print(f"Here's the {cipher_direction}d result: {end_text}")

# from art import logo
# print(logo)

# should_end = False
# while not should_end:

#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))
#   shift = shift % 26
#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#   restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#   if restart == "no":
#     should_end = True
#     print("Goodbye")

# =========================================================================================================================
# My Updated code.
# # from day_8_art import logo

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # print(logo)


# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for char in start_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift_amount
#             # print(new_position)
#             if new_position > len(alphabet):
#                 new_shift_index = new_position % len(alphabet)
#                 end_text += alphabet[new_shift_index]
#             else:
#                 end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f"Here's the {cipher_direction}d result: {end_text}")
    

# acc_input = True
# while acc_input is True:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     shift = shift % 26
#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#     user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
#     if user_input == 'no':
#         print("Bye.")
#         acc_input = False