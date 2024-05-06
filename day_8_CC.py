alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    decode_text = ""
    for letter in text:
        shift_index = alphabet.index(letter) + shift
        # print(shift_index)

        if shift_index >= len(alphabet):
            new_shift_index = shift_index - len(alphabet)
            # print(new_shift_index)
            decode_text += alphabet[new_shift_index]
            # decode_text.append(alphabet[new_shift_index])
        else:
            decode_text += alphabet[shift_index]
            # decode_text.append(alphabet[shift_index])


    print(f"The encoded text is {''.join(decode_text)}.")
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(text, shift):


  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

    encode_text = ""
    for letter in text:
        shift_index = alphabet.index(letter) - shift
        # print(shift_index)

        if shift_index < 0:
            new_shift_index = len(alphabet) + shift_index
            # print(new_shift_index)
            encode_text += alphabet[new_shift_index]
            # decode_text.append(alphabet[new_shift_index])
        else:
            encode_text += alphabet[shift_index]
            # decode_text.append(alphabet[shift_index])

    print(f"The encoded text is {''.join(encode_text)}.")
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Ivalid Input.")
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


