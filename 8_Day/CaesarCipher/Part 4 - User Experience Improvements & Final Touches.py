
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
    
""" Here is the explanation for the code above:
1. We create a variable called 'alphabet' and assign it a string of all the letters in the English alphabet.
2. We create a function called 'caesar' that takes three inputs:
  - 'start_text' which is the plain text or the cipher text that needs to be encrypted or decrypted.
  - 'shift_amount' which is the number of letters to shift the alphabet.
  - 'cipher_direction' which tells the program whether to encrypt or decrypt the start_text.
3. We create an empty string variable called 'end_text' that will eventually hold the encrypted or decrypted version of the 'start_text'.
4. We make the program able to encrypt 'decode' as well as decrypt 'encode' text by creating an if statement that checks the value of 'cipher_direction' and changes the value of 'shift_amount' to negative if the direction is 'decode'.
5. We create a for loop that loops through each letter in the 'start_text' and find its corresponding position in the 'alphabet' by using the index() method.
6. We create a variable called 'new_position' which is equal to the 'position' of the current letter plus the 'shift_amount'.
7. We use the modulo operator (%) to make sure that the new_position stays within the range of 0-25.
8. We add the new letter (new_position) to 'end_text'.
9. We print the encrypted or decrypted text to the console.
10. We check if the user input is a letter or not using the 'in' keyword.
11. If the user input is not a letter, we just add it to 'end_text' without changing it. """
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift %= 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  result = input("Type 'yes' if you wanna continue or 'No' to stop! ")
  if result == "No":
    should_continue = False
    print("Goodbye")
      