#CODE FOR ENCRYPTING

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def caesar(plain_text, shift_amount, cypher):
  cipher_text = ""
  if cypher.lower() == "decode":
      shift_amount *= -1
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The {direction}d text is {cipher_text}")



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(plain_text = text, shift_amount = shift, cypher = direction)