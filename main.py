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

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
      
  
  # for each letter in text
  # find that letter in alphabet list
  #   new_text = letter[current index + shift]

  # join letters to form the encrypted_word
    #print(new_text)
  

  
#OUTPUT
  #plain_text = "hello"
  #shift = 5
  #cipher_text = "mjqqt"
  #print output: "The encoded text is mjqqt"

