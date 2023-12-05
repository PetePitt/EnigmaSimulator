from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma

# historical enigma rotors and reflectors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO","V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# key board and pugboard
KB = Keyboard()
PB = Plugboard(["AB", "CD", "EF"])

# define enigma machine
ENIGMA = Enigma(B,IV,II,I,PB,KB)

#set the rings
ENIGMA.set_rings((5,26,2))

# set message key
ENIGMA.set_key("CAT")

#encipher a message
message = "THISCOOLENIGMAMACHINE"
cipher_text = ""
for letter in message:
    cipher_text = cipher_text + ENIGMA.encipher(letter)
print(cipher_text)

