#CODE FOR ENCRYPTING

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text,shift):
  text_list = list(text.strip(""))
  text_encoded = ""
  for char in text_list:
    if char in alphabet:
      current_index = alphabet.index(char)
      new_index = current_index + shift
      new_char = alphabet[new_index]
      text_encoded += new_char
  print(f"The encoded text is {text_encoded}")
encrypt(text,shift)

def decrypt(text,shift):
  text_list = list(text.strip(""))
  text_encoded = ""
  for char in text_list:
      current_index = alphabet.index(char)
      new_index = current_index - shift
      if new_index < 0:
                new_index = 26 - new_index
      new_char = alphabet[new_index]
      text_encoded += new_char
  print(f"The decrypted text is {text_encoded}")

if direction.lower() == "encode":
  encrypt(text,shift)
elif direction.lower() == "decode":
  decrypt(text,shift)
else:
  print("You have entered an invalid option")